from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' + os.getenv("SAY_HI")

if __name__ == '__main__':
    app.run(port=4983,host='0.0.0.0',debug=True)
