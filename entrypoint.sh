#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn bamm.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3