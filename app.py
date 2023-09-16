from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world! The page was created by Chekhovska Maryna.'
