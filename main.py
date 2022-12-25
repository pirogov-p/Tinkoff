import pymysql
from connect import host,user,password,db_name


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

        with connection.cursor() as cursor:
            delete_query = "DELETE FROM transaction WHERE id_transaction >= 20 AND id_transaction < 30;"
            cursor.execute(delete_query)
            connection.commit()

        with connection.cursor() as cursor:
            for a in range(4):
                insert_list2 = (
                "INSERT INTO tinkoff.transaction (id_transaction, price_paper, paper_count,transaction_type,paper_id,run_dt)"
                "VALUES (%s, %s, %s, %s,%s,%s)"
                )
                data = (a+20, 20*a, 20-a,'sell',2,'1991-03-21')
                cursor.execute(insert_list2, data)
            connection.commit()


        with connection.cursor() as cursor:
            sql = "SELECT * FROM tinkoff.transaction "
            cursor.execute(sql)
            result = cursor.fetchall()
            for a in result:
                print(a)

    finally:
        connection.close()

except Exception as ex:
    print('ERROR')

