# flask 数据库
# pip install flask-sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

class Config:
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Dslr#2024@10.10.250.3:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

# SQLAlchemy 和 app 绑定起来
db = SQLAlchemy(app)

# 创建数据库模型类
class Role(db.Model):
    """角色表"""
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return '%s' % self.name

class User(db.Model):
    """用户表"""
    __tablename__ = 'user'
    # 默认设置自增长
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    # 表关系 一对多 外键 ForeignKey 用来关联另外一张表
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return '%s' % self.name


if __name__ == '__main__':
    with app.app_context():
        # 清除所有表
        db.drop_all()
        # 创建所有的表
        db.create_all()

        # 创建对象 插入数据
        role1 = Role(name='admin')
        # session 记录到对象任务中
        db.session.add(role1)
        # 提交任务
        db.session.commit()

        # 创建对象 插入数据
        role2 = Role(name='admin2')
        # session 记录到对象任务中
        db.session.add(role2)
        # 提交任务
        db.session.commit()

        user1 = User(name='zhangsan', password='123', role_id=role1.id)
        user2 = User(name='lisi', password='345', role_id=role1.id)

        # 关联第二个角色
        user3 = User(name='wangwu', password='123', role_id=role2.id)

        db.session.add_all([user1, user2, user3])
        db.session.commit()

