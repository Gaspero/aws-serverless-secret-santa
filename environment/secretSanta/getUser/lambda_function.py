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
                userId = str(payload.get('userId'))
                # получаем записанную запись по переданным параметрам
                # sql = "SELECT * FROM public.users WHERE id=%s"
                sql = """
                    SELECT 
                    	public.users.id,
                    	public.users.name,
                    	public.users.email,
                    	public.desiredGiftRelation.giftId,
                    	rel1.receiverId,
                    	rel2.secretSantaId
                    FROM public.users
                    LEFT JOIN public.desiredGiftRelation ON public.users.id = public.desiredGiftRelation.userId
                    LEFT JOIN public.secretSantaRelation as rel1 ON public.users.id = rel1.secretSantaId
                    LEFT JOIN public.secretSantaRelation as rel2 ON public.users.id = rel2.receiverId
                    WHERE public.users.id=%s
                """
                cursor.execute(sql, userId)
                result = cursor.fetchone()
                return (result)
        finally:
            connection.close()
        
    operations = {
        'GET':   lambda payload: queryDB(payload)
    }
        
    operation = event['httpMethod']
        
    if operation in operations:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
        return respond(None, operations[operation](payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
