from app import app

if __name__ == "__main__":
    app.run()

# gunicorn --workers 4 --bind unix:app.sock --daemon -m 007 --user www-data --worker-class gevent wsgi:app