#!/usr/bin/env bash

sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart

sudo gunicorn -b 0.0.0.0:8000 --pythonpath='/home/box/web/ask/ask/' wsgi &
sudo gunicorn -b 0.0.0.0:8080 --pythonpath='/home/box/web/' hello:app &
#sudo gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
#sudo gunicorn -c /home/box/web/etc/django.py wsgi --daemon
