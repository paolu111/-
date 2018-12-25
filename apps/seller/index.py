from apps.forms.company import Business_Form
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


# 添加企业
@seller_log_bp.route("/info/", endpoint="info", methods=["GET", "POST"])
def info_com():
    if request.method == "GET":
        form = Business_Form(request.form)
        return render_template("info.html", form=form, title="企业信息")
    if request.method == "POST":
        form = Business_Form(request.form)
        if form.validate():
            data = request.form
            b1 = Business()
            b1.setattrs(form.data)
            db.session.add(b1)
            db.session.commit()
            return "ok"
        return "off"


# 查看企业
@seller_log_bp.route("/show_com/", endpoint="show_com", methods=["GET", "POST"])
def show_comp():
    if request.method == "GET":
        buss = Business.query.all()
        return render_template("breeding.html", buss=buss)


# 删除企业
@seller_log_bp.route("/del_comp/<comp_id>/", endpoint="del_comp", methods=["GET", "POST"])
def del_comp(comp_id):
    comp_id = int(comp_id)
    b1 = Business.query.filter_by(id=comp_id).delete()
    db.session.commit()
    return "ok"


# 更新企业
@seller_log_bp.route("/update_comp/<comp_id>/", endpoint="update_comp", methods=["GET", "POST"])
def update_comp(comp_id):
    comp_id = int(comp_id)
    b1 = Business.query.filter_by(id=comp_id).first()
    if not b1:
        return "没有该企业"
    if request.method == "POST":
        form = Business_Form(request.form)
        if form.validate():
            b1 = Business()
            b1.setattrs(form.data)
            db.session.add(b1)
            db.session.commit()
            return "ok"
    else:
        form = Business_Form(data=dict(b1))
    return render_template("info.html", form=form)
