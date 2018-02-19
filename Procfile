release: python manage.py migrate
web: gunicorn pawz.wsgi --log-file -
worker: python worker.py