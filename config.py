# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlckqa'
USERNAME = 'root'
PASSWORD = 'Qq199797'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "Qq19977997990820520"

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '465'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = '1293859278@qq.com'
MAIL_PASSWORD = 'hrlduapvcfsshefg'
MAIL_DEFAULT_SENDER = '1293859278@qq.com'
