# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /backend

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use Node.js as base image
FROM node:18

# Set working directory
WORKDIR /frontend

# Copy package.json and package-lock.json
COPY ./frontend/package.json ./frontend/package-lock.json ./

# Install dependencies
RUN npm install --force

# Copy application code
COPY ./frontend .

# Build the application
RUN npm run build

# Expose Next.js port
EXPOSE 3000

# Command to start the application
CMD ["npm", "start"]
