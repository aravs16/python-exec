from flask import Flask
from flask_cors import CORS
import sqlite3
import json


app = Flask(__name__)
CORS(app)



@app.route('/')
def hello():
    return "Hello From Server!"

@app.route('/addtodo/<todo>')
def addtodo(todo):
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos VALUES ('"+todo+"')")
    conn.commit()
    conn.close()
    return "SUCCESS"

@app.route('/gettodos/')
def gettodos():
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("SELECT rowid, todo FROM todos")
    todos = c.fetchall()
    todo_array = []
    for t in todos:
        todo_array.append(t[1])
    return json.dumps(todo_array)

app.run(port="1309")