#!/usr/bin/env bash
# Apply database migrations
python manage.py migrate
# Collect static files (optionnel si tu les utilises)
python manage.py collectstatic --noinput
