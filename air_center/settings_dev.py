from .base_settings import *
import configparser

config = configparser.ConfigParser()
config.read('conf/database.conf')

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# 获取数据库连接信息
db_name = config['DEFAULT']['NAME']
db_user = config['DEFAULT']['USER']
db_password = config['DEFAULT']['PASSWORD']
db_host = config['DEFAULT'].get('HOST', 'localhost')
db_port = config['DEFAULT'].getint('PORT', 3306)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}


