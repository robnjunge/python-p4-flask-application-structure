#!/usr/bin/env python3

# the value of __name__ when running python server/app.py
# is '__main__', which is the name of the module app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# can also run development server from the command line
# through treating our application module as a script 
# with the app.run() method
if __name__ == '__main__':
    app.run(port=5555, debug=True)