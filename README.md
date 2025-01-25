# Quantm - Quantitive Massar 📈

Quantm is a full-stack dashboard application developed to showcase financial and operational insights. Built using **Django** for the backend and **Next.js** for the frontend, Quantm demonstrates modern full-stack development principles and provides an intuitive user experience.

---

## Features

- **Interactive Dashboard**: Visualize key data and insights.
- **Backend**: Built with Django for robust API and data management.
- **Frontend**: Dynamic and responsive UI with Next.js.
- **Data Visualization**: Present insights using charts and graphs.
- **Environment Management**: Configured for both development and production environments.

---

## Tech Stack

### Backend
- Django
- Django REST Framework (DRF)
- PostgreSQL

### Frontend
- Next.js
- Tailwind CSS

### Deployment
- Docker for containerized environments
- Vercel for frontend hosting

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker (optional)

### Backend Setup
1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations and run the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
5. Access the backend at `http://localhost:8000`.

### Frontend Setup
1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
4. Access the frontend at `http://localhost:3000`.

---

## Environment Variables

### Backend
Create a `.env` file in the `backend/` directory with the following variables:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Frontend
Create a `.env.local` file in the `frontend/` directory with the following variable:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

---

## Testing

### Backend Tests
1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Run tests using `pytest`:
   ```bash
   pytest
   ```

### Frontend Tests
1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```
2. Run tests using `Jest`:
   ```bash
   npm run test
   ```

---

## Contact

For any questions or further information, feel free to reach out:

- **Email**: [shahsuvarli.elvin@gmail.com](mailto:shahsuvarli.elvin@gmail.com)
- **LinkedIn**: [LinkedIn](http://linkedin.com/in/shahsuvarli/)

---

**Quantm - A Full-Stack Dashboard Application by Elvin Shahsuvarli**

