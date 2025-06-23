# 🏥 Healthcare Backend System

A **secure, scalable, and RESTful API** built using **Django** and **Django REST Framework** for managing healthcare data including patients, doctors, and their relationships.

---

## 🚀 Key Features

### 🔐 Authentication & Security
- JWT-based authentication
- Secure registration and login
- Password encryption
- Token refresh support

### 👤 User Management
- Custom user model (email-based)
- Email verification on registration
- Secure password storage

### 🧑‍⚕️ Doctor Management
- CRUD operations on doctor profiles
- Tracks specialization, license, and experience

### 👩‍⚕️ Patient Management
- Full CRUD support for patients
- Tracks personal details & medical history
- Access control for users

### 🔗 Patient-Doctor Mapping
- Assign doctors to patients
- View mapping with visit reasons
- One-to-many and many-to-one support

---

## 🛠️ Tech Stack

- **Backend**: Django 4.2+, Django REST Framework 3.14+
- **Database**: PostgreSQL (prod), SQLite (dev)
- **Auth**: JWT (`djangorestframework-simplejwt`)
- **Others**: `python-decouple`, `django-cors-headers`, `psycopg2-binary`

---

## ⚙️ Setup Guide

### 🔧 Prerequisites
- Python 3.8+
- PostgreSQL (for production)
- Git

---

### 📝 Step-by-Step Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend

# Create and activate a virtual environment
python -m venv healthcare_env
source healthcare_env/bin/activate  # For Windows: healthcare_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### 🔐 Environment Configuration

Create a `.env` file in the root:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=healthcare_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

---

### 🗃️ Database Setup

**PostgreSQL**:
```sql
CREATE DATABASE healthcare_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO postgres;
```

**SQLite (dev)**: In `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

### 🔨 Run Migrations & Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### ▶️ Start Development Server

```bash
python manage.py runserver
```

API will be available at: [http://localhost:8000/](http://localhost:8000/)

---

## 📡 API Endpoints

### 🔐 Authentication

- **Register**: `POST /api/auth/register/`
- **Login**: `POST /api/auth/login/`
- **Refresh Token**: `POST /api/auth/token/refresh/`

### 🏥 Patients

| Action       | Endpoint                  | Method |
|--------------|---------------------------|--------|
| Create       | `/api/patients/`          | POST   |
| List All     | `/api/patients/`          | GET    |
| Get by ID    | `/api/patients/{id}/`     | GET    |
| Update       | `/api/patients/{id}/`     | PUT    |
| Delete       | `/api/patients/{id}/`     | DELETE |

### 👨‍⚕️ Doctors

| Action       | Endpoint                  | Method |
|--------------|---------------------------|--------|
| Create       | `/api/doctors/`           | POST   |
| List All     | `/api/doctors/`           | GET    |
| Get by ID    | `/api/doctors/{id}/`      | GET    |
| Update       | `/api/doctors/{id}/`      | PUT    |
| Delete       | `/api/doctors/{id}/`      | DELETE |

### 🔗 Patient-Doctor Mapping

| Action               | Endpoint                             | Method |
|----------------------|--------------------------------------|--------|
| Assign Doctor        | `/api/mappings/`                     | POST   |
| List All Mappings    | `/api/mappings/`                     | GET    |
| Get Patient's Doctors| `/api/mappings/patient/{patient_id}/`| GET    |
| Delete Mapping       | `/api/mappings/{id}/`                | DELETE |

---

## 🧬 Database Models

### 🔹 User
- `email`, `name`, `password`, `is_active`, `is_staff`, `created_at`

### 🔹 Patient
- Linked to User
- Includes `first_name`, `dob`, `gender`, `medical_history`, etc.

### 🔹 Doctor
- Linked to User
- Includes `specialization`, `license_number`, `years_of_experience`

### 🔹 PatientDoctorMapping
- `patient`, `doctor`, `assigned_by`, `reason_for_visit`

---

## 🧪 Testing

### ✅ Run Unit Tests
```bash
python manage.py test
```

### 🧪 Postman & cURL
Example (cURL - Register User):

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{
  "email": "test@example.com",
  "name": "Test User",
  "password": "testpass123"
}'
```

---

## 🚀 Deployment Tips

- Set `DEBUG = False`
- Use **PostgreSQL**
- Secure `.env` & `SECRET_KEY`
- Use HTTPS in production

---

## 📬 Contact

**Developer**: Rishav Upadhyay  
**Email**: [rishavupadhyay482@gmail.com](mailto:rishavupadhyay482@gmail.com)
