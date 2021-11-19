from flask import Flask, request
from controllers import Controllers

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sign")
def sign_message():
    return Controllers.getMessageSignature(request.args.get('message'))