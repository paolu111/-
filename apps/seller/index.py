from apps.seller import seller_log_bp
from flask import render_template


@seller_log_bp.route('/', endpoint='index')
def index():
    return 'index'