from pydoc import apropos
import re
from flask import Flask, render_template, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/')
def index():
    return "index"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return f"{escape(username)}'s profile"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello2(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
def do_the_login():
    return "-> code for login"

def show_the_login_form():
    return "-> code for login form"