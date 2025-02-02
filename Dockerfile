FROM python:3.11 AS backend

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend .

FROM node:18 AS frontend

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend .
RUN npm run build

FROM python:3.11 AS final

WORKDIR /app/backend

COPY --from=backend /app /app/backend

COPY --from=frontend /app/.next /app/frontend/.next

RUN apt-get update && apt-get install -y nodejs npm

EXPOSE 8000 3000

CMD ["sh", "-c", "pip install -r /app/backend/requirements.txt && npm install --prefix /app/frontend && gunicorn app.wsgi:application --bind 0.0.0.0:8000 & npm start --prefix /app/frontend"]

