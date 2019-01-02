from wtforms import Form, StringField, validators


class User_Form(Form):
    name = StringField(label="用户名", validators=[validators.DataRequired(message="必填项")],
                       render_kw={"class": "layui-input"}
                       )
    password = StringField(label="密码", validators=[validators.DataRequired(message="必填项")],
                           render_kw={"class": "layui-input"}
                           )
