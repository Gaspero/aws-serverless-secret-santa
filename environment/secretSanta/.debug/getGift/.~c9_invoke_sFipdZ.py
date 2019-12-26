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

# подключаемся к БД
connection = pymysql.connect(host=host,
                             user=username,
                             password=password,
                             db='public',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def lambda_handler(event, context):
    try:
        with connection.cursor() as cursor:
            userId = event.get('userId')
            # получаем записанную запись по переданным параметрам
            sql = "SELECT * FROM public.users WHERE id=%s"
            cursor.execute(sql, (userId))
            result = cursor.fetchone()
    finally:
        connection.close()

    return (result)
