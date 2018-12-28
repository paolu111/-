from flask import g

from apps.models.seller_models import Cate_Business


def get_cate(old_func):
    def nener(*args, **kwargs):
        cates = Cate_Business.query.all()
        g.bus_cates = cates
        ret = old_func(*args, **kwargs)
        return ret

    return nener
