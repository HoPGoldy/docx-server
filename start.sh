#! /bin/sh

PYTHONPATH=`pwd`/src gunicorn --workers 4 --bind unix:app.sock --daemon -m 007 --user www-data --worker-class gevent wsgi:app
nginx
tail -f /var/log/nginx/access.log