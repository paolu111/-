from wtforms import Form, StringField, validators, SelectField

from apps.models.seller_models import Cate_Business


class Business_Form(Form):
    name = StringField(label="公司名称", validators=[validators.DataRequired(message="必填项")],
                       render_kw={"class": "layui-input"}
                       )
    boss = StringField(label="法人姓名", validators=[validators.DataRequired(message="必填项")],
                       render_kw={"class": "layui-input"}
                       )
    tel = StringField(label="公司电话", validators=[validators.DataRequired(message="必填项")],
                      render_kw={"class": "layui-input"}
                      )
    email = StringField(label="公司邮箱", validators=[validators.DataRequired(message="必填项")],
                        render_kw={"class": "layui-input"}
                        )
    type = SelectField(label="公司类型", coerce=int, render_kw={"class": "layui-input"})

    def __init__(self, *args, **kwargs):
        cates = Cate_Business.query.all()
        super(Business_Form, self).__init__(*args, **kwargs)
        self.type.choices = [(i.id, i.name) for i in cates]
