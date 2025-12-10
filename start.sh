#!/bin/bash

set -e

echo "Starting Django application..."

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Load fixtures if they exist and database is empty
echo "Loading initial data..."
python manage.py loaddata fixtures.json || echo "No fixtures to load or already loaded"

# Create superuser if needed
echo "Creating admin user..."
python manage.py create_admin || echo "Admin user already exists or creation failed"

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:${PORT:-8000} config.wsgi:application