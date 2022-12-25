import pymysql
from openapi_client import openapi

from connect import host,user,password,db_name,token

token = token
client = openapi.api_client(token)
pf = client.portfolio.portfolio_get()

print(pf)

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('CONNECT!')

    try:
        #with connection.cursor() as cursor:




        with connection.cursor() as cursor:
            sql = "SELECT * FROM tinkoff.paper "
            cursor.execute(sql)
            result = cursor.fetchall()
            #for a in result:
               # print(a)

    finally:
        connection.close()

except Exception as ex:
    print('ERROR')