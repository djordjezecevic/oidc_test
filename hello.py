from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World 3!'


#set FLASK_ENV=development
#set FLASK_APP=hello.py
