#!/usr/bin/env bash
# Exit on error
set -o errexit

# Start the Django application with Gunicorn
cd lms_core
gunicorn lms_core.wsgi:application
