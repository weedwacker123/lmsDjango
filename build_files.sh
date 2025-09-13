#!/bin/bash

# Build script for Vercel deployment
echo "Building Django project for Vercel..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3.9 lms_core/manage.py collectstatic --noinput --clear

# Create staticfiles_build directory for Vercel
mkdir -p staticfiles_build
cp -r staticfiles/* staticfiles_build/
