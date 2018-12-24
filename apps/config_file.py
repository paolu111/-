import os
from redis import Redis


base_dir = os.path.abspath(os.path.dirname(__file__))


class DevBase(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class ProductBase(object):
    DEBUG = False


def get_redis_address():
    return Redis(host="127.0.0.1", port=6388)


class DevConfig(DevBase):
    SESSION_TYPE = 'redis'
    # SESSION_REDIS = Redis(host='127.0.0.1', port=6388)
    # QINIU_ACCESS_KEY = 'P64sj-fGTlrZLvhZD3pWs3cWLxKf0R0revClvXzQ'
    # QINIU_SECRET_KEY = 'LWrFrtUTHxeir2QEATRa_4iTKjhdoHVmz35NdNY3'
    # QINIU_BUCKET_NAME = 'white'
    # QINIU_BUCKET_DOMAIN = 'pht7x5lcj.bkt.clouddn.com'



