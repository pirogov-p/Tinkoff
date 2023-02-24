import pymysql
from datetime import datetime
from openapi_client import openapi

from connect import host,user,password,db_name,token1

token = token1
client = openapi.api_client(token)

cd2 = datetime(2022, 12, 25)
cd1 = datetime(2021, 12, 25)
print(cd2)
print(cd1)

cur = client.market.market_currencies_get()


print(cur)
#cur = client.market.market_candles_get('BBG0013HGFT4', cd1, cd2, 'day')
#for a in pf.payload.positions:
#    print(a)
#instr = client.market.market_currencies_get()
#print(instr)
#print(cur)
'''try:
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




        with connection.cursor() as cursor:
            sql = "SELECT * FROM tinkoff.paper "
            cursor.execute(sql)
            result = cursor.fetchall()
            #for a in result:
               # print(a)

    finally:
        connection.close()

except Exception as ex:
    print('ERROR')'''