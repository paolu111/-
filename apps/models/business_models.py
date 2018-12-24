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
    tel =db.Column(db.Integer)
    # 企业邮箱
    email = db.Column(db.String(32))