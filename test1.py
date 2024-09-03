
import os
import pymysql.cursors 
connection = pymysql.connect(host=os.getenv("DB_HOST"),
user=os.getenv("DB_USER"),
password=os.getenv("DB_PASSWD"),
database=os.getenv("DB_NAME"),
cursorclass=pymysql.cursors.DictCursor) 
