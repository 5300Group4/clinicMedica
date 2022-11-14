 #!/bin/bash
 # 从第一行到最后一行分别表示：
 # 1. 生成数据库迁移文件
 # 2. 根据数据库迁移文件来修改数据库
 # 3. 用 uwsgi启动 django 服务, 不再使用python manage.py runserver
 python manage.py makemigrations&&
 python manage.py migrate&&
 uwsgi --ini /var/www/html/mysite2/uwsgi.ini
 # python manage.py runserver 0.0.0.0:8000