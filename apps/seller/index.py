from apps.seller import seller_log_bp
from flask import render_template


@seller_log_bp.route('/', endpoint='business_manager')
def business_manager():
    return render_template('business_manager.html')


@seller_log_bp.route('/login', endpoint='login')
def login():
    return render_template('login.html')
