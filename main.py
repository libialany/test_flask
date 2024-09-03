from  flask import Flask,request,render_template,redirect,url_for,flash
import os
import pymysql.cursors
app = Flask(__name__)
app.secret_key = os.getenv('key')
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def hello_world():
    # bookmarks=[]
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM links")
    #     bookmarks=cursor.fetchall()    
    # return bookmarks
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=4983,host='0.0.0.0',debug=True)
