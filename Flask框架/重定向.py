# 重定向 302

from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/index')
def index():
    return redirect(url_for('hello'))

@app.route('/')
def hello():
    return 'This is a hello'

if __name__ == '__main__':
    app.run()
