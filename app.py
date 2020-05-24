from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/createdb/<dbname>')
def create(dbname):
    #create db
    return "Hello "+name

@app.route('/insert/<todo>')
def insert(todo):
    # insert todo
    return "Hello "+name

@app.route('/getalltodos')
def getalltodos():
    # get todos
    return "Hello "+name

app.run()