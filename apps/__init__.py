from flask_session import Session
from flask_login import LoginManager
from flask import Flask

login_manager = LoginManager()



def crea_db(app):
    from apps.models import db
    db.init_app(app)


def register_bp(app):
    from apps.seller import seller_log_bp
    app.register_blueprint(seller_log_bp)


def crete_app(set):
    app = Flask(__name__, static_url_path='/static', static_folder='paolu_static')
    app.config.from_object(set)
    # 指定session的保存位置
    Session(app=app)
    # flask_login插件的使用
    # login_manager.init_app(app=app)
    # login_manager.login_view = "seller.logins"
    crea_db(app)
    register_bp(app)

    return app

