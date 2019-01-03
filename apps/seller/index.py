from apps.forms.company import Business_Form
from apps.lib.tool_func import get_cate
from apps.models import db
from apps.models.seller_models import Business
from apps.seller import seller_log_bp
from flask import render_template, request, g, redirect, url_for
from flask_login import login_required, current_user


@seller_log_bp.route('/', endpoint='business_manager')
def business_manager():
    return render_template('business/business_manager.html')


@seller_log_bp.route('/login', endpoint='login')
def login():
    return render_template('login.html')


# 添加企业
@seller_log_bp.route("/info/", endpoint="info", methods=["GET", "POST"])
@get_cate
@login_required
def info_com():
    cates = g.bus_cates
    if request.method == "GET":
        form = Business_Form(request.form)
        return render_template("business/info.html", cates=cates, form=form, title="企业信息")
    if request.method == "POST":
        user = current_user.id
        form = Business_Form(request.form)
        if form.validate():
            data = request.form
            b1 = Business()
            b1.setattrs(form.data)
            # 用户与企业关联
            b1.admin = user
            db.session.add(b1)
            db.session.commit()
            return redirect(url_for("seller.show_comp"))
        return redirect(url_for("seller.info"))


# 查看分类企业
@seller_log_bp.route("/show_com/<cate_bus_id>/", endpoint="show_com", methods=["GET"])
@get_cate
@login_required
def show_comp(cate_bus_id):
    cates = g.bus_cates
    cate_bus_id = int(cate_bus_id)
    buss = Business.query.filter_by(admin=current_user.id, type=cate_bus_id).all()
    return render_template("business/breeding.html", cates=cates, buss=buss)


# 查看企业
@seller_log_bp.route("/show_com/", endpoint="show_comp", methods=["GET"])
@get_cate
@login_required
def show_comp():
    cates = g.bus_cates
    buss = Business.query.filter_by(admin=current_user.id).all()
    return render_template("business/breeding.html", cates=cates, buss=buss)


# 删除企业
@seller_log_bp.route("/del_comp/<comp_id>/", endpoint="del_comp", methods=["GET", "POST"])
@get_cate
@login_required
def del_comp(comp_id):
    comp_id = int(comp_id)
    b1 = Business.query.filter_by(admin=current_user.id, id=comp_id).delete()
    db.session.commit()
    return redirect("seller.show_com")


# 更新企业
@seller_log_bp.route("/update_comp/<comp_id>/", endpoint="update_comp", methods=["GET", "POST"])
@get_cate
@login_required
def update_comp(comp_id):
    comp_id = int(comp_id)
    b1 = Business.query.filter_by(admin=current_user.id, id=comp_id).first()
    cates = g.bus_cates
    if not b1:
        return "没有该企业"
    if request.method == "POST":
        form = Business_Form(request.form)
        if form.validate():
            b1 = Business()
            b1.setattrs(form.data)
            db.session.add(b1)
            db.session.commit()
            return redirect("seller.show_com")
    else:
        form = Business_Form(data=dict(b1))
    return render_template("business/info.html", cates=cates, form=form)
