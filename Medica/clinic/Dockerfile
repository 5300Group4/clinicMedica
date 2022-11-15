# 基础镜像：python3.7 环境，也可使用python3.7-alphine缩小镜像体积
FROM python:3.7

# 镜像作者
MAINTAINER DJG

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 在容器内/var/www/html/下创建 mysite3文件夹
RUN mkdir -p /var/www/html/clinic

# 设置容器内工作目录
WORKDIR /var/www/html/clinic

# 将当前目录文件拷贝一份到工作目录中（. 表示当前目录）
ADD . /var/www/html/clinic

# 利用 pip 安装依赖
RUN pip install -r requirements.txt

# Windows环境下编写的start.sh每行命令结尾有多余的\r字符，需移除。
RUN sed -i 's/\r//' ./start.sh

# 设置start.sh文件可执行权限
RUN chmod +x ./start.sh