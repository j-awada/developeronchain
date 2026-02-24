#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
#python manage.py compress
#python manage.py collectstatic --no-input

gunicorn developeronchain.wsgi:application --bind 0.0.0.0:8000