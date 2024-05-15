# Airdrop data center

## Setup

## Django env

pip install djangorestframework


## Django

使用 DJANGO_SETTINGS_MODULE 环境变量指定要加载的配置文件


在开发环境：
DJANGO_SETTINGS_MODULE=air_center.settings_dev
在生产环境：
DJANGO_SETTINGS_MODULE=air_center.settings_prod

### run django

python manage.py makemigrations --settings air_center.settings_dev
python manage.py migrate --settings air_center.settings_dev

### unit test

python manage.py test --settings air_center.settings_dev


