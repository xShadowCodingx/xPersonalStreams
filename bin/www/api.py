# This is the main API entry point

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO"

