SQLALCHEMY_DATABASE_URI = \
    "postgresql://db_user:db_pass@localhost/database"

SQLALCHEMY_TRACK_MODIFICATIONS = True

IMGUR_ID = "xxx"
IMGUR_SECRET = "yyy"


try:
    from local_settings import *
except ImportError:
    pass