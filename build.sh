#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Load initial data fixtures
python manage.py loaddata fixtures.json

# Create admin user automatically
python manage.py create_admin

# Collect static files
python manage.py collectstatic --noinput

echo "✅ Build completed successfully!"
echo "🔑 Admin login: username=admin, password=admin123"