#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Change to Django project directory
cd lms_core

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Go back to root directory
cd ..
