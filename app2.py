from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Hello From Server!"

@app.route('/mypath/')
def hello2():
    return "<h1>Hello World 2</h1>"

app.run(port="1307")