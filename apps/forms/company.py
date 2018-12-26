from wtforms import Form, StringField, validators


class Business_Form(Form):
    name = StringField(label="公司名称", validators=[validators.DataRequired(message="必填项")],
                       render_kw={"class":"layui-input"}
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
