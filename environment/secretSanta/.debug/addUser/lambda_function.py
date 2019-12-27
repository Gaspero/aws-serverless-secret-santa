import pymysql.cursors
import boto3
import json

def get_secret():

    secret_name = "MySQL"
    region_name = "us-east-1"

    # Создаем клиент Secrets Manager
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name)
        SecretString = json.loads(get_secret_value_response["SecretString"])
        username = SecretString["username"]
        password = SecretString["password"]
        host = SecretString["host"]
        return(username, password, host)
        
    except Exception as e:
        raise e

username, password, host = get_secret()

def lambda_handler(event, context):
    
    def respond(err, res=None):
        return {
            'statusCode': 400 if err else 200,
            'body': json.dumps(str(err)) if err else json.dumps(res)
        }

    def queryDB(payload):
        # подключаемся к БД
        connection = pymysql.connect(host=host,
                                     user=username,
                                     password=password,
                                     db='public',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        
        try:
            with connection.cursor() as cursor:
                # добавляем в БД запись
                sql = "INSERT INTO public.users(name, email) VALUES (%s, %s)"
                # получаем параметры из запроса
                name = payload.get('name')
                print(name)
                email = payload.get('email')
                print(email)
                cursor.execute(sql, (name, email))
        
            # коммитим изменениея
            result = connection.commit()
        
            with connection.cursor() as cursor:
                # получаем записанную запись по переданным параметрам
                sql = "SELECT * FROM public.users WHERE name=%s AND email=%s"
                cursor.execute(sql, (name, email))
                result = cursor.fetchone()
                print(result)
        finally:
            connection.close()
    
        return (result)
        
    operations = {
        'POST':   lambda payload: queryDB(payload)
    }
        
    operation = event['httpMethod']
    print(operation)
        
    if operation in operations:
        payload = json.loads(event['body']) if operation == 'POST' else json.loads('')
        return respond(None, operations[operation](payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
