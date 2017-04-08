#!/bin/sh

cd django_app
rm -rf staticfiles
python manage.py collectstatic --noinput
python manage.py flush --noinput
python manage.py migrate
#python manage.py populatedb --createsuperuser
python manage.py runserver 0.0.0.0:8000
