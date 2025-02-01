#!/bin/bash
set -e

# --- Start the Django backend ---
cd backend
# Run migrations and collect static files (adjust these commands as needed)
# python manage.py migrate --noinput
# python manage.py collectstatic --noinput
# Launch Django on port 8000 in the background
python manage.py runserver 0.0.0.0:8000 &

# --- Start the Next.js frontend ---
cd ../frontend
# Launch the Next.js production server (ensure your package.json has a "start" script)
npm run start
