#!/bin/bash
# 从第一行到最后一行分别表示：
# 1. 收集静态文件到根目录
# 2. 生产数据库迁移文件
# 3. 根据数据库迁移文件来修改数据库
# 4. 用 uwsgi启动 django 服务, 不再使用python manage.py runserver
python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
uwsgi --ini /var/www/html/mysite3/uwsgi.ini