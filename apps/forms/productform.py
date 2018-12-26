from wtforms import Form, StringField, BooleanField, IntegerField, validators, DecimalField, SelectField


class ProductForm(Form):

    name = StringField(label='产品名',
                             validators=[validators.DataRequired(message='输入产品名称'),
                                         validators.length(max=20, message='名字字数不能超过20')
                                         ],
                             )


    #下拉框
    # cate = SelectField(label="所属产品分类", validators=[validators.DataRequired("必填项")],
    #                      # render_kw={'class': 'form-control'}, coerce=str,
    #                       )

    # def __init__(self, user, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.cate.choices = [(x.Pro_cate.id, x.cate_name) for x in user.shop]
