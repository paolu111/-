from apps.forms.login import User_Form
from apps.models import db
from apps.seller import seller_log_bp
from flask import request, render_template, redirect, url_for
from apps.models.user import SellerModel
from flask_login import login_user, logout_user


@seller_log_bp.route('/register/', endpoint='register', methods=['GET', 'POST'])
def user_register():
    if request.method == "POST":
        u1 = SellerModel()
        # u1.setattrs(request.form)
        data = request.form
        u1.name = data.get("username")
        u1.accout = data.get("auth")
        u1.password = data.get("password")
        db.session.add(u1)
        db.session.commit()
        return redirect(url_for('seller.logins'))
    return render_template('register.html')


@seller_log_bp.route('/logins/', endpoint='logins', methods=['GET', 'POST'])
def user_login():
    form = User_Form(request.form)
    if request.method == "POST" and form.validate():
        s1 = SellerModel.query.filter_by(name=form.data.get("name")).first()
        if s1 and s1.check_password(form.data.get("password")):
            login_user(s1)
            next_url = request.args.get("next", '')
            if not next_url.startswith("/"):
                next_url = None
            return redirect(next_url or url_for("seller.show_comp"))
        return "用户名或密码错误"
    return render_template('login.html', form=form, title="用户登录")
