# Base image for backend (Django)
FROM python:3.11 AS backend

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend .

# Base image for frontend (Next.js)
FROM node:18 AS frontend

# Set working directory
WORKDIR /app

# Install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy frontend code and build
COPY frontend .
RUN npm run build

# Final image
FROM python:3.11 AS final

WORKDIR /app/backend

# Copy backend from first stage
COPY --from=backend /app /app/backend

# Copy frontend build from second stage
COPY --from=frontend /app/.next /app/frontend/.next

RUN apt-get update && apt-get install -y nodejs npm

# Expose ports
EXPOSE 8000 3000

# Run backend and frontend
CMD ["sh", "-c", "pip install -r /app/backend/requirements.txt && npm install --prefix /app/frontend && gunicorn app.wsgi:application --bind 0.0.0.0:8000 & npm start --prefix /app/frontend"]

