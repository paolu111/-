from apps.models import BaseModel
from apps.models import db


# 企业表
class Business(BaseModel):
    # 企业名称
    name = db.Column(db.String(32))
    # 省
    province = db.Column(db.String(32))
    # 市
    city = db.Column(db.String(32))
    # 县
    county = db.Column(db.String(32))
    # 详细地址
    address = db.Column(db.String(32))
    # 经度
    longitude = db.Column(db.Float)
    # 纬度
    latitude = db.Column(db.Float)
    # 法人
    boss = db.Column(db.String(32))
    # 企业电话
    tel = db.Column(db.String(16))
    # 企业邮箱
    email = db.Column(db.String(32))
    # 企业类型
    type = db.Column(db.String(16))

    def keys(self):
        return "name", "boss", "tel", "email"


# 产品分类表
class Pro_cate(BaseModel):
    cate_name = db.Column(db.String(32))


# 产品表
class Product(BaseModel):
    # 产品名称
    name = db.Column(db.String(32))
    # 产品类型
    pro_type = db.Column(db.String(32))
    # 质量特色
    quality = db.Column(db.String(128))
    # 生产工艺
    craft = db.Column(db.String(128))
    # 产品规格
    size = db.Column(db.String(32))
    # 产地
    place = db.Column(db.String(32))
    # 保质期
    expiration = db.Column(db.String(32))
    # 是否是假冒伪劣
    fake = db.Column(db.Boolean, default=False)
    # 产品分类
    category = db.Column(db.Integer, db.ForeignKey(Pro_cate.id))
    cate = db.relationship("Pro_cate", backref="product")
    # 产品企业
    business = db.Column(db.Integer, db.ForeignKey(Business.id))
    busin = db.relationship("Business", backref="product")
