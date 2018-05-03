FROM frolvlad/alpine-python3
# 维护者
MAINTAINER Fu Zhaohui<fuzhaohui200@gmail.com>
# Bundle app source
ADD . /src/app
# 设置工作目录
WORKDIR /src/app
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "Application.py" ]