import pymysql.cursors
import boto3

def get_secret():

    secret_name = "MySQL"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name)
        print(getattr(get_secret_value_response, "SecretString.username"))
        # print(get_secret_value_response.SecretString.username, get_secret_value_response.SecretString.password)
    except Exception as e:
        raise e

get_secret()

# подключаемся к БД
connection = pymysql.connect(host='database-mysql.cpu0sqttgot5.us-east-1.rds.amazonaws.com',
                             user='admin',
                             password='Doglover4',
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
