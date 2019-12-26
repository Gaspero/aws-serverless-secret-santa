{"filter":false,"title":"lambda_function.py","tooltip":"/secretSanta/addUser/lambda_function.py","undoManager":{"mark":68,"position":68,"stack":[[{"start":{"row":30,"column":35},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":4},"end":{"row":32,"column":0},"action":"insert","lines":["",""]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":32,"column":4},"end":{"row":39,"column":9},"action":"insert","lines":["def respond(err, res=None):","      return {","            'statusCode': '400' if err else '200',","            'body': err.message if err else json.dumps(res),","            'headers': {","                'Content-Type': 'application/json',","            },","        }"],"id":3}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "],"id":5}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":5},"action":"insert","lines":["d"],"id":6},{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["e"]},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":[" "],"id":7}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["q"],"id":8},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["u"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["e"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["r"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["y"]}],[{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["B"],"id":9}],[{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"remove","lines":["B"],"id":10}],[{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["D"],"id":11},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":["N"]}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"remove","lines":["N"],"id":12}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":["B"],"id":13}],[{"start":{"row":41,"column":15},"end":{"row":41,"column":17},"action":"insert","lines":["()"],"id":14}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":[":"],"id":15}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"remove","lines":[":"],"id":16}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":[":"],"id":17}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "],"id":18},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"insert","lines":["    "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"insert","lines":["    "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":4},"action":"insert","lines":["    "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":4},"action":"insert","lines":["    "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":4},"action":"insert","lines":["    "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":4},"action":"insert","lines":["    "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"insert","lines":["    "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":4},"action":"insert","lines":["    "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"insert","lines":["    "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"insert","lines":["    "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"insert","lines":["    "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"insert","lines":["    "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"insert","lines":["    "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":4},"action":"insert","lines":["    "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"insert","lines":["    "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["    "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":["n"],"id":19},{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":["a"]},{"start":{"row":41,"column":18},"end":{"row":41,"column":19},"action":"insert","lines":["m"]},{"start":{"row":41,"column":19},"end":{"row":41,"column":20},"action":"insert","lines":["e"]},{"start":{"row":41,"column":20},"end":{"row":41,"column":21},"action":"insert","lines":[","]}],[{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":[" "],"id":20},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["e"]},{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"insert","lines":["m"]},{"start":{"row":41,"column":24},"end":{"row":41,"column":25},"action":"insert","lines":["a"]},{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"insert","lines":["i"]},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["l"]}],[{"start":{"row":41,"column":20},"end":{"row":41,"column":21},"action":"insert","lines":[":"],"id":21},{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["s"]},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":21},"end":{"row":41,"column":23},"action":"remove","lines":["st"],"id":22},{"start":{"row":41,"column":21},"end":{"row":41,"column":24},"action":"insert","lines":["str"]}],[{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"insert","lines":[":"],"id":23},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["s"]},{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["t"]},{"start":{"row":41,"column":34},"end":{"row":41,"column":35},"action":"insert","lines":["r"]}],[{"start":{"row":71,"column":23},"end":{"row":72,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":72,"column":0},"end":{"row":72,"column":8},"action":"insert","lines":["        "]},{"start":{"row":72,"column":8},"end":{"row":73,"column":0},"action":"insert","lines":["",""]},{"start":{"row":73,"column":0},"end":{"row":73,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":73,"column":4},"end":{"row":73,"column":8},"action":"remove","lines":["    "],"id":25}],[{"start":{"row":73,"column":4},"end":{"row":73,"column":35},"action":"insert","lines":["operation = event['httpMethod']"],"id":26}],[{"start":{"row":73,"column":35},"end":{"row":74,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":74,"column":4},"end":{"row":75,"column":33},"action":"insert","lines":["if operation == \"POST\":","        arguments = event[\"body\"]"],"id":28}],[{"start":{"row":71,"column":23},"end":{"row":72,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":72,"column":0},"end":{"row":72,"column":8},"action":"insert","lines":["        "]},{"start":{"row":72,"column":8},"end":{"row":73,"column":0},"action":"insert","lines":["",""]},{"start":{"row":73,"column":0},"end":{"row":73,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":73,"column":4},"end":{"row":73,"column":8},"action":"remove","lines":["    "],"id":30}],[{"start":{"row":73,"column":4},"end":{"row":76,"column":5},"action":"insert","lines":["operations = {","        'GET':    lambda: load_to_bucket(),","        'POST':   lambda payload: change_and_load(payload)","    }"],"id":31}],[{"start":{"row":74,"column":8},"end":{"row":74,"column":43},"action":"remove","lines":["'GET':    lambda: load_to_bucket(),"],"id":32},{"start":{"row":74,"column":4},"end":{"row":74,"column":8},"action":"remove","lines":["    "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"remove","lines":["    "]},{"start":{"row":73,"column":18},"end":{"row":74,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":74,"column":34},"end":{"row":74,"column":49},"action":"remove","lines":["change_and_load"],"id":33},{"start":{"row":74,"column":34},"end":{"row":74,"column":41},"action":"insert","lines":["queryDB"]}],[{"start":{"row":77,"column":35},"end":{"row":78,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":78,"column":0},"end":{"row":78,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":80,"column":33},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":81,"column":0},"end":{"row":81,"column":8},"action":"insert","lines":["        "]},{"start":{"row":81,"column":8},"end":{"row":82,"column":0},"action":"insert","lines":["",""]},{"start":{"row":82,"column":0},"end":{"row":82,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":82,"column":4},"end":{"row":82,"column":8},"action":"remove","lines":["    "],"id":36}],[{"start":{"row":82,"column":4},"end":{"row":86,"column":79},"action":"insert","lines":["if operation in operations:","        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])","        return respond(None, operations[operation](payload))","    else:","        return respond(ValueError('Unsupported method \"{}\"'.format(operation)))"],"id":37}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":35},"action":"remove","lines":["name:str, email:str"],"id":38},{"start":{"row":41,"column":16},"end":{"row":41,"column":23},"action":"insert","lines":["payload"]}],[{"start":{"row":79,"column":0},"end":{"row":80,"column":33},"action":"remove","lines":["    if operation == \"POST\":","        arguments = event[\"body\"]"],"id":39},{"start":{"row":78,"column":4},"end":{"row":79,"column":0},"action":"remove","lines":["",""]},{"start":{"row":78,"column":0},"end":{"row":78,"column":4},"action":"remove","lines":["    "]},{"start":{"row":77,"column":35},"end":{"row":78,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":80,"column":66},"end":{"row":80,"column":69},"action":"remove","lines":["GET"],"id":40},{"start":{"row":80,"column":66},"end":{"row":80,"column":67},"action":"insert","lines":["P"]},{"start":{"row":80,"column":67},"end":{"row":80,"column":68},"action":"insert","lines":["o"]},{"start":{"row":80,"column":68},"end":{"row":80,"column":69},"action":"insert","lines":["s"]},{"start":{"row":80,"column":69},"end":{"row":80,"column":70},"action":"insert","lines":["t"]}],[{"start":{"row":80,"column":69},"end":{"row":80,"column":70},"action":"remove","lines":["t"],"id":41},{"start":{"row":80,"column":68},"end":{"row":80,"column":69},"action":"remove","lines":["s"]},{"start":{"row":80,"column":67},"end":{"row":80,"column":68},"action":"remove","lines":["o"]}],[{"start":{"row":80,"column":67},"end":{"row":80,"column":68},"action":"insert","lines":["O"],"id":42},{"start":{"row":80,"column":68},"end":{"row":80,"column":69},"action":"insert","lines":["S"]},{"start":{"row":80,"column":69},"end":{"row":80,"column":70},"action":"insert","lines":["T"]}],[{"start":{"row":80,"column":77},"end":{"row":80,"column":101},"action":"remove","lines":["json.loads(event['body']"],"id":43}],[{"start":{"row":80,"column":77},"end":{"row":80,"column":78},"action":"insert","lines":["p"],"id":44},{"start":{"row":80,"column":78},"end":{"row":80,"column":79},"action":"insert","lines":["a"]},{"start":{"row":80,"column":79},"end":{"row":80,"column":80},"action":"insert","lines":["s"]},{"start":{"row":80,"column":80},"end":{"row":80,"column":81},"action":"insert","lines":["s"]}],[{"start":{"row":80,"column":77},"end":{"row":80,"column":81},"action":"remove","lines":["pass"],"id":45}],[{"start":{"row":80,"column":77},"end":{"row":80,"column":79},"action":"insert","lines":["''"],"id":46}],[{"start":{"row":80,"column":78},"end":{"row":80,"column":80},"action":"insert","lines":["''"],"id":47}],[{"start":{"row":80,"column":78},"end":{"row":80,"column":80},"action":"remove","lines":["''"],"id":48}],[{"start":{"row":80,"column":18},"end":{"row":80,"column":48},"action":"remove","lines":["event['queryStringParameters']"],"id":49},{"start":{"row":80,"column":18},"end":{"row":80,"column":42},"action":"insert","lines":["json.loads(event['body']"]}],[{"start":{"row":55,"column":23},"end":{"row":55,"column":28},"action":"remove","lines":["event"],"id":50},{"start":{"row":55,"column":23},"end":{"row":55,"column":30},"action":"insert","lines":["payload"]}],[{"start":{"row":56,"column":24},"end":{"row":56,"column":29},"action":"remove","lines":["event"],"id":51},{"start":{"row":56,"column":24},"end":{"row":56,"column":31},"action":"insert","lines":["payload"]}],[{"start":{"row":55,"column":42},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":56,"column":0},"end":{"row":56,"column":16},"action":"insert","lines":["                "]},{"start":{"row":56,"column":16},"end":{"row":56,"column":17},"action":"insert","lines":["p"]},{"start":{"row":56,"column":17},"end":{"row":56,"column":18},"action":"insert","lines":["r"]},{"start":{"row":56,"column":18},"end":{"row":56,"column":19},"action":"insert","lines":["i"]},{"start":{"row":56,"column":19},"end":{"row":56,"column":20},"action":"insert","lines":["n"]},{"start":{"row":56,"column":20},"end":{"row":56,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":56,"column":21},"end":{"row":56,"column":23},"action":"insert","lines":["()"],"id":53}],[{"start":{"row":56,"column":22},"end":{"row":56,"column":23},"action":"insert","lines":["a"],"id":54}],[{"start":{"row":56,"column":22},"end":{"row":56,"column":23},"action":"remove","lines":["a"],"id":55}],[{"start":{"row":56,"column":22},"end":{"row":56,"column":23},"action":"insert","lines":["n"],"id":56},{"start":{"row":56,"column":23},"end":{"row":56,"column":24},"action":"insert","lines":["a"]},{"start":{"row":56,"column":24},"end":{"row":56,"column":25},"action":"insert","lines":["m"]},{"start":{"row":56,"column":25},"end":{"row":56,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":57,"column":44},"end":{"row":58,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":58,"column":0},"end":{"row":58,"column":16},"action":"insert","lines":["                "]},{"start":{"row":58,"column":16},"end":{"row":58,"column":17},"action":"insert","lines":["p"]},{"start":{"row":58,"column":17},"end":{"row":58,"column":18},"action":"insert","lines":["r"]},{"start":{"row":58,"column":18},"end":{"row":58,"column":19},"action":"insert","lines":["i"]},{"start":{"row":58,"column":19},"end":{"row":58,"column":20},"action":"insert","lines":["n"]},{"start":{"row":58,"column":20},"end":{"row":58,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":58,"column":21},"end":{"row":58,"column":23},"action":"insert","lines":["()"],"id":58}],[{"start":{"row":58,"column":22},"end":{"row":58,"column":23},"action":"insert","lines":["e"],"id":59},{"start":{"row":58,"column":23},"end":{"row":58,"column":24},"action":"insert","lines":["m"]},{"start":{"row":58,"column":24},"end":{"row":58,"column":25},"action":"insert","lines":["a"]},{"start":{"row":58,"column":25},"end":{"row":58,"column":26},"action":"insert","lines":["i"]},{"start":{"row":58,"column":26},"end":{"row":58,"column":27},"action":"insert","lines":["l"]}],[{"start":{"row":79,"column":35},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":80,"column":0},"end":{"row":80,"column":4},"action":"insert","lines":["    "]},{"start":{"row":80,"column":4},"end":{"row":80,"column":5},"action":"insert","lines":["p"]},{"start":{"row":80,"column":5},"end":{"row":80,"column":6},"action":"insert","lines":["r"]},{"start":{"row":80,"column":6},"end":{"row":80,"column":7},"action":"insert","lines":["i"]},{"start":{"row":80,"column":7},"end":{"row":80,"column":8},"action":"insert","lines":["n"]},{"start":{"row":80,"column":8},"end":{"row":80,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":80,"column":9},"end":{"row":80,"column":11},"action":"insert","lines":["()"],"id":61}],[{"start":{"row":80,"column":10},"end":{"row":80,"column":11},"action":"insert","lines":["o"],"id":62},{"start":{"row":80,"column":11},"end":{"row":80,"column":12},"action":"insert","lines":["p"]},{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":10},"end":{"row":80,"column":13},"action":"remove","lines":["ope"],"id":63},{"start":{"row":80,"column":10},"end":{"row":80,"column":19},"action":"insert","lines":["operation"]}],[{"start":{"row":80,"column":20},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":64},{"start":{"row":81,"column":0},"end":{"row":81,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":81,"column":4},"end":{"row":81,"column":28},"action":"insert","lines":["json.loads(event['body']"],"id":65}],[{"start":{"row":81,"column":4},"end":{"row":81,"column":5},"action":"insert","lines":["p"],"id":66},{"start":{"row":81,"column":5},"end":{"row":81,"column":6},"action":"insert","lines":["r"]},{"start":{"row":81,"column":6},"end":{"row":81,"column":7},"action":"insert","lines":["i"]},{"start":{"row":81,"column":7},"end":{"row":81,"column":8},"action":"insert","lines":["n"]},{"start":{"row":81,"column":8},"end":{"row":81,"column":9},"action":"insert","lines":["t"]},{"start":{"row":81,"column":9},"end":{"row":81,"column":10},"action":"insert","lines":["("]}],[{"start":{"row":81,"column":34},"end":{"row":81,"column":35},"action":"insert","lines":[")"],"id":67}],[{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"insert","lines":[")"],"id":68}],[{"start":{"row":0,"column":0},"end":{"row":88,"column":0},"action":"remove","lines":["import pymysql.cursors","import boto3","import json","","def get_secret():","","    secret_name = \"MySQL\"","    region_name = \"us-east-1\"","","    # Создаем клиент Secrets Manager","    session = boto3.session.Session()","    client = session.client(","        service_name='secretsmanager',","        region_name=region_name","    )","","    try:","        get_secret_value_response = client.get_secret_value(","            SecretId=secret_name)","        SecretString = json.loads(get_secret_value_response[\"SecretString\"])","        username = SecretString[\"username\"]","        password = SecretString[\"password\"]","        host = SecretString[\"host\"]","        return(username, password, host)","        ","    except Exception as e:","        raise e","","username, password, host = get_secret()","","def lambda_handler(event, context):","    ","    def respond(err, res=None):","      return {","            'statusCode': '400' if err else '200',","            'body': err.message if err else json.dumps(res),","            'headers': {","                'Content-Type': 'application/json',","            },","        }","","    def queryDB(payload):","        # подключаемся к БД","        connection = pymysql.connect(host=host,","                                     user=username,","                                     password=password,","                                     db='public',","                                     charset='utf8mb4',","                                     cursorclass=pymysql.cursors.DictCursor)","        ","        try:","            with connection.cursor() as cursor:","                # добавляем в БД запись","                sql = \"INSERT INTO public.users(name, email) VALUES (%s, %s)\"","                # получаем параметры из запроса","                name = payload.get('name')","                print(name)","                email = payload.get('email')","                print(email)","                cursor.execute(sql, (name, email))","        ","            # коммитим изменениея","            result = connection.commit()","        ","            with connection.cursor() as cursor:","                # получаем записанную запись по переданным параметрам","                sql = \"SELECT * FROM public.users WHERE name=%s AND email=%s\"","                cursor.execute(sql, (name, email))","                result = cursor.fetchone()","                print(result)","        finally:","            connection.close()","    ","        return (result)","        ","    operations = {","        'POST':   lambda payload: queryDB(payload)","    }","        ","    operation = event['httpMethod']","    print(operation)","    print(json.loads(event['body']))","        ","    if operation in operations:","        payload = json.loads(event['body'] if operation == 'POST' else '')","        return respond(None, operations[operation](payload))","    else:","        return respond(ValueError('Unsupported method \"{}\"'.format(operation)))",""],"id":69},{"start":{"row":0,"column":0},"end":{"row":85,"column":0},"action":"insert","lines":["import pymysql.cursors","import boto3","import json","","def get_secret():","","    secret_name = \"MySQL\"","    region_name = \"us-east-1\"","","    # Создаем клиент Secrets Manager","    session = boto3.session.Session()","    client = session.client(","        service_name='secretsmanager',","        region_name=region_name","    )","","    try:","        get_secret_value_response = client.get_secret_value(","            SecretId=secret_name)","        SecretString = json.loads(get_secret_value_response[\"SecretString\"])","        username = SecretString[\"username\"]","        password = SecretString[\"password\"]","        host = SecretString[\"host\"]","        return(username, password, host)","        ","    except Exception as e:","        raise e","","username, password, host = get_secret()","","def lambda_handler(event, context):","    ","    def respond(err, res=None):","        return {","            'statusCode': 400 if err else 200,","            'body': err.message if err else json.dumps(res)","        }","","    def queryDB(payload):","        # подключаемся к БД","        connection = pymysql.connect(host=host,","                                     user=username,","                                     password=password,","                                     db='public',","                                     charset='utf8mb4',","                                     cursorclass=pymysql.cursors.DictCursor)","        ","        try:","            with connection.cursor() as cursor:","                # добавляем в БД запись","                sql = \"INSERT INTO public.users(name, email) VALUES (%s, %s)\"","                # получаем параметры из запроса","                name = payload.get('name')","                print(name)","                email = payload.get('email')","                print(email)","                cursor.execute(sql, (name, email))","        ","            # коммитим изменениея","            result = connection.commit()","        ","            with connection.cursor() as cursor:","                # получаем записанную запись по переданным параметрам","                sql = \"SELECT * FROM public.users WHERE name=%s AND email=%s\"","                cursor.execute(sql, (name, email))","                result = cursor.fetchone()","                print(result)","        finally:","            connection.close()","    ","        return (result)","        ","    operations = {","        'POST':   lambda payload: queryDB(payload)","    }","        ","    operation = event['httpMethod']","    print(operation)","    print(json.loads(event['body']))","        ","    if operation in operations:","        payload = json.loads(event['body']) if operation == 'POST' else json.loads('')","        return respond(None, operations[operation](payload))","    else:","        return respond(ValueError('Unsupported method \"{}\"'.format(operation)))",""]}],[{"start":{"row":35,"column":12},"end":{"row":35,"column":59},"action":"remove","lines":["'body': err.message if err else json.dumps(res)"],"id":70},{"start":{"row":35,"column":12},"end":{"row":35,"column":68},"action":"insert","lines":["'body': json.dumps(str(err)) if err else json.dumps(res)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":35,"column":68},"end":{"row":35,"column":68},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1577317330131,"hash":"0312728892a12caf9f4b37fd80f925553ba7f3ae"}