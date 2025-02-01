# Use a slim Python image as the base
FROM python:3.11-slim

# Install system utilities and Node.js (using Node 16)
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    # Update npm to the latest major version to remove the notice
    npm install -g npm@11.1.0 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy both backend and frontend directories into the image
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# --- Build the Django backend ---
# Switch to the backend folder, upgrade pip, and install dependencies.
WORKDIR /app/backend
RUN pip install --upgrade pip && pip install -r requirements.txt

# --- Build the Next.js frontend ---
# Switch to the frontend folder, install node modules, and build the app.
WORKDIR /app/frontend
RUN npm install --force && npm run build

# --- Prepare the startup script ---
# Go back to the project root and copy the startup script into the image.
WORKDIR /app
COPY start.sh .
RUN chmod +x start.sh

# Expose ports: Django (8000) and Next.js (3000)
EXPOSE 8000 3000

# Start both services when the container launches.
CMD ["./start.sh"]
