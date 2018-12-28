from apps.models import BaseModel, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

loginmanager = LoginManager()


class SellerModel(BaseModel, UserMixin):
    # 人名
    name = db.Column(db.String(32))
    # 账号
    accout = db.Column(db.String(32))
    # 密码
    _password = db.Column('password', db.String(128))
    # 权限 0:普通用户， 1：企业， 2：管理员
    authority = db.Column(db.Integer,default=1)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val)

    def check_password(self, data):
        return check_password_hash(self.password, data)

    def my_setattr(self, data):
        for k, v in data.items():
            if hasattr(self, k) and k != id:
                setattr(self, k, v)


@loginmanager.user_loader
def load_user(userid: str):
    return SellerModel.query.get(int(userid))
