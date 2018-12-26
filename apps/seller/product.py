from flask import request, render_template

from apps.models import db
from apps.models.seller_models import Product
from apps.seller import seller_log_bp


@seller_log_bp.route("/product/", endpoint="product", methods=["GET", "POST"])
def pro_add():
    if request.method == "GET":
        return render_template("product/pro_add.html")
    elif request.method == "POST":
        data = request.form
        p1 = Product()
        p1.name = data.get("name")
        p1.category = int(data.get("category"))
        p1.business = int(data.get("business"))
        db.session.add(p1)
        db.session.commit()
        return "ok"


@seller_log_bp.route("/show_pro/", endpoint="show_pro", methods=["GET"])
def show_pro():
    p1 = Product.query.all()
    return render_template("product/show_pro.html", p1=p1)
