from apps.models import db
from apps.models.seller_models import Business
from apps.seller import seller_log_bp
from flask import render_template, request


@seller_log_bp.route('/', endpoint='business_manager')
def business_manager():
    return render_template('business_manager.html')


@seller_log_bp.route('/login', endpoint='login')
def login():
    return render_template('login.html')



@seller_log_bp.route("/info/", endpoint="info", methods=["GET","POST"])
def info_com():
    if request.method=="GET":
        return render_template("info.html")
    if request.method=="POST":
        data = request.form
        b1 = Business()
        b1.name = data.get("name")
        b1.email = data.get("email")
        db.session.add(b1)
        db.session.commit()
        return "ok"

@seller_log_bp.route("/show_com/",endpoint="show_com",methods=["GET","POST"])
def show_comp():
    buss = Business.query.all()
    return render_template("show_comp.html", buss=buss)

