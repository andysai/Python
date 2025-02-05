# 自定义转换器
import typing as t

from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的方法
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        # 父类的方法，功能一ing实现好了
        print("to_python的方法被调用")
        return value

# 将自定义的转换器类添加到flask应用中
app.url_map.converters['re'] = RegexConverter

@app.route('/index/<re("123"):value>')
# @app.route('/index/<re("1\d{10}"):value>')
def index(value):
    print(value)
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

