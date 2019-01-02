from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, default=0)

    def setattrs(self, obj):
        for k, v in obj.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)


from apps.models import seller_models
from apps.models import user
