
import os
import pymysql.cursors 
connection = pymysql.connect(host=os.getenv("DB_HOST"),
user=os.getenv("DB_USER"),
password=os.getenv("DB_PASSWD"),
database=os.getenv("DB_NAME"),
cursorclass=pymysql.cursors.DictCursor) 
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM links"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)   
except Exception as e:
    print(e)