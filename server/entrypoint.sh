#!/bin/sh

echo "Applying migrations..."
python manage.py makemigrations djangoapp --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
