from flask import Blueprint


seller_log_bp = Blueprint('seller', __name__)


from apps.seller import index
from apps.seller import product
from apps.seller import auth
