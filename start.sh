#! /bin/sh

PYTHONPATH=`pwd`/src gunicorn \
--workers 4 \
--bind unix:app.sock \
--daemon -m 007 \
--user www-data \
--log-level debug \
--access-logfile /home/flask-server/access.log \
--error-logfile /home/flask-server/error.log \
--worker-class gevent wsgi:app

nginx

tail -f /home/flask-server/access.log