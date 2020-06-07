from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Iam app 1"

app.run(port="1306")