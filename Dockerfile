# Use a slim Python image as the base for the backend
FROM python:3.11-slim AS backend

# Install system utilities
RUN apt-get update && apt-get install -y curl gnupg && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set backend working directory
WORKDIR /app/backend

# Copy backend files
COPY backend/ .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose backend port
EXPOSE 8000

# Use a separate Node.js image for the frontend
FROM node:20 AS frontend

# Set frontend working directory
WORKDIR /app/frontend

# Copy frontend files
COPY frontend/ .

# Install dependencies and build the Next.js app
RUN npm install --force && npm run build

# Serve the Next.js app using a lightweight server
RUN npm install -g serve

# Expose frontend port
EXPOSE 3000

# Final stage to combine both services
FROM python:3.11-slim

# Set up the working directory
WORKDIR /app

# Copy backend from backend stage
COPY --from=backend /app/backend /app/backend

# Copy frontend from frontend stage
COPY --from=frontend /app/frontend /app/frontend

# Environment variables for connecting to Supabase
ENV DATABASE_URL="your_supabase_database_url"

# Start Django backend and serve the Next.js frontend
CMD ["sh", "-c", "cd /app/backend && python manage.py migrate && gunicorn app.wsgi:application --bind 0.0.0.0:8000"]
