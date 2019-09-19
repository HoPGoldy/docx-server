FROM ubuntu:18.04

MAINTAINER hopgoldy@gmail.com

RUN apt-get update -y && \
    apt-get install python3 python3-pip nginx -y && \
    apt-get clean && \
    mkdir /home/flask-server

WORKDIR /home/flask-server

EXPOSE 80

COPY . /home/flask-server

RUN rm /etc/nginx/sites-enabled/default && \
    cp /home/flask-server/nginx_setting /etc/nginx/sites-enabled/default && \
    pip3 install -r requirements.txt

CMD ["sh", "start.sh"]