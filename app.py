from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>jobs: translator, sportsperson, </p><p>pays: france, allemagne, espagne,</p><p>nouvelle d'une destination : </p><p>conversations:</p><p>photos:</p>"
