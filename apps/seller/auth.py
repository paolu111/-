from apps.models import db
from apps.seller import seller_log_bp
from flask import request, render_template, redirect, url_for
from apps.models.user import SellerModel


@seller_log_bp.route('/register/', endpoint='register', methods=['GET', 'POST'])
def user_register():
    if request.method == "POST":
        u1 = SellerModel()
        # u1.setattrs(request.form)
        data = request.form
        u1.name = data.get("username")
        u1.password = data.get("password")
        db.session.add(u1)
        db.session.commit()
        return redirect(url_for('user_login'))
    return render_template('register.html')


@seller_log_bp.route('/logins/', endpoint='logins', methods=['GET', 'POST'])
def user_login():
    return render_template('login.html')
