
import os
from  flask import Flask,request,render_template,redirect,url_for,flash
import pymysql.cursors 
connection = pymysql.connect(host=os.getenv("DB_HOST"),
user=os.getenv("DB_USER"),
password=os.getenv("DB_PASSWD"),
database=os.getenv("DB_NAME"),
cursorclass=pymysql.cursors.DictCursor) 
app = Flask(__name__)
app.secret_key = os.getenv('key')
app.config['SESSION_TYPE'] = 'filesystem'
@app.route('/')
def hello_world():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM links"
            cursor.execute(sql)
            result = cursor.fetchall()  
    except Exception as e:
        print(e)
    return result

if __name__ == '__main__':
    app.run(port=4983,host='0.0.0.0',debug=True)
