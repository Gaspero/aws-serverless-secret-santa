import pymysql.cursors
import boto3
import json
from urllib.parse import unquote_plus

s3 = boto3.client('s3')

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
    
    def queryDB(name):
        # подключаемся к БД
        connection = pymysql.connect(host=host,
                                     user=username,
                                     password=password,
                                     db='public',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        
        try:
            with connection.cursor() as cursor:
                # добавляем запись в базу
                sql = "INSERT INTO public.gifts(name, url) VALUES (%s, %s)"
                url = "https://secret-santa-static-images.s3.amazonaws.com/"+name
                cursor.execute(sql, (name, url))
                result = cursor.fetchone()
                result = connection.commit()
    
            with connection.cursor() as cursor:
                # получаем записанную запись по переданным параметрам
                sql = "SELECT * FROM public.gifts WHERE name=%s AND url=%s"
                cursor.execute(sql, (name, url))
                result = cursor.fetchone()
                return (result)
               
        finally:
            connection.close()
    
    def get_records(event):
        for record in event['Records']:
            key = unquote_plus(record['s3']['object']['key'])
            added_row = queryDB(key)
            return(added_row)
            
    return get_records(event)

