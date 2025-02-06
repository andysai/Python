from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = '<KEY>'
class Register(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='再一次输入密码', validators=[DataRequired('密码不能为空'),EqualTo('password')])
    submit = SubmitField(label='提交')

@app.route('/register', methods=['GET','POST'])
def register():
    # 创建表单对象
    form = Register()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        # validate_on_submit 验证器 表单传过来的数据如果是正确的就会往后面执行
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data
            print(username)
            print(password)
            print(password2)
        else:
            print("验证失败")
        return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

