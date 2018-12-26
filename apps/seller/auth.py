from apps.models import db
from apps.seller import seller_log_bp
from flask import request, render_template, redirect, url_for,session
from apps.models.user import SellerModel
from apps.forms.userform import RegisterSellerForm, LoginSellerForm
from flask_login import login_user, login_required, logout_user


@seller_log_bp.route('/register/', endpoint='register', methods=['GET', 'POST'])
def user_register():
    form = RegisterSellerForm(request.form)
    if request.method == "POST" and form.validate():
        u1 = SellerModel()
        u1.my_setattr(form.data)
        db.session.add(u1)
        db.session.commit()
        return redirect(url_for('seller.logins'))
    return render_template('register.html', form=form, flags="注册")


@seller_log_bp.route('/logins/', endpoint='logins', methods=['GET', 'POST'])
def user_login():
    form = LoginSellerForm(request.form)
    if request.method == "POST" and form.validate():
        u1 = SellerModel.query.filter_by(accout=form.accout.data).first()
        if u1 and u1.check_password(form.password.data):
            # 保存session,session配置在init文件
            # login_user(u1)
            return redirect(url_for('seller.business_manager'))
        else:
            form.password.errors=["输入密码错误"]
    return render_template('register.html', form=form, flags="登录")

# @seller_log_bp.route('/logout/', endpoint='logout')
# @login_required
# def seller_logout():
#     logout_user()
#     session.clear()
#     return redirect(url_for('cms.index'))