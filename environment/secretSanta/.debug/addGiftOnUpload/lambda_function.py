import pymysql.cursors

def lambda_handler(event, context):

    # подключаемся к БД
    connection = pymysql.connect(host='database-mysql.cpu0sqttgot5.us-east-1.rds.amazonaws.com',
                                 user='admin',
                                 password='Doglover4',
                                 db='public',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            # добавляем в БД запись
            sql = "INSERT INTO public.gifts(name, url) VALUES (%s, %s)"
            # получаем параметры из запроса
            name = event.get('name')
            url = "https://secret-santa-static-images.s3.amazonaws.com/"+name
            cursor.execute(sql, (name, url))
    
        # коммитим изменениея
        result = connection.commit()
    
        with connection.cursor() as cursor:
            # получаем записанную запись по переданным параметрам
            sql = "SELECT * FROM public.users WHERE name=%s AND url=%s"
            cursor.execute(sql, (name, url))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

    return (result)
