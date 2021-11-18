import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:" + SECRET_KEY + "@127.0.01/books_db"
    DEBUG = True
    CSRF_ENABLED = True
