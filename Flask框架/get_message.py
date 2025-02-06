from sqlalchemy.sql.functions import current_user

from flask数据库 import *
from sqlalchemy import and_

# with app.app_context():
#     user = User.query.all()
# print(user)
#
# with app.app_context():
#     user = User.query.get(1)
# print(user)
#
# with app.app_context():
#     user = User.query.count()
# print(user)
#
# with app.app_context():
#     user = User.query.filter(User.name == 'zhangsan').all()
# print(user)

# with app.app_context():
#     user = User.query.filter(User.name.like('%a%')).all()
# print(user)

# with app.app_context():
#     user = User.query.filter(and_(User.name == 'zhangsan', User.id == 1)).all()
#     print(user)

with app.app_context():
    user = User.query.get(1)
    print(user)
