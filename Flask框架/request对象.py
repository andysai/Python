# request 包含前端发送过来的所有请求数据
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('password')
        print(name, passwd)
        return 'This is Post'

if __name__ == '__main__':
    app.run()
