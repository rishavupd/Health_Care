The Healthcare Backend System is a comprehensive RESTful API built with Django and Django REST Framework that provides a secure platform for managing healthcare data. The system allows healthcare providers to register, authenticate, and manage patient records, doctor information, and patient-doctor relationships.

Key Objectives
Provide secure user authentication using JWT tokens
Enable CRUD operations for patient and doctor records
Manage patient-doctor assignments
Ensure data privacy and security
Offer scalable architecture for healthcare applications

Features
🔐 Authentication & Security
JWT-based authentication system
Secure user registration and login
Token refresh mechanism
Password encryption using Django's built-in system

👥 User Management
Custom user model with email-based authentication
User registration with email verification
Secure password management

🏥 Patient Management
Create, read, update, and delete patient records
Comprehensive patient information storage
Medical history tracking
User-specific patient access control

👨‍⚕️ Doctor Management
Complete doctor profile management
Specialization and license tracking
Years of experience recording
Secure doctor information storage

🔗 Patient-Doctor Mapping
Assign doctors to patients
Track reasons for visits
View all doctors assigned to a patient
Manage multiple patient-doctor relationships
Technology Stack

Backend Framework
Django 4.2+: High-level Python web framework
Django REST Framework 3.14+: Powerful toolkit for building Web APIs

Database
PostgreSQL: Primary production database
SQLite: Development database option

Authentication
djangorestframework-simplejwt: JSON Web Token authentication

Additional Libraries
python-decouple: Environment variable management
django-cors-headers: Cross-Origin Resource Sharing handling
psycopg2-binary: PostgreSQL adapter for Python

Installation Guide
Prerequisites
Python 3.8 or higher
PostgreSQL (for production) or SQLite (for development)
Git

Step 1: Clone the Repository
BASH

git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend

Step 2: Create Virtual Environment
BASH

# Create virtual environment
python -m venv healthcare_env

# Activate virtual environment
# On Windows
healthcare_env\Scripts\activate
# On macOS/Linux
source healthcare_env/bin/activate
Step 3: Install Dependencies
BASH

pip install -r requirements.txt
Step 4: Environment Configuration
Create a .env file in the project root:

ENV

SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
DATABASE_NAME=healthcare_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
Step 5: Database Setup
For PostgreSQL:
BASH

# Create database (in PostgreSQL shell)
CREATE DATABASE healthcare_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO postgres;
For SQLite (Development):
Update settings.py:

Python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Step 6: Run Migrations
BASH

python manage.py makemigrations
python manage.py migrate
Step 7: Create Superuser
BASH

python manage.py createsuperuser
Step 8: Run Development Server
BASH

python manage.py runserver
The API will be available at http://localhost:8000/

API Documentation
Base URL

http://localhost:8000/api/
Authentication Endpoints
1. User Registration
URL: /api/auth/register/
Method: POST
Body:
JSON

{
    "email": "user@example.com",
    "name": "John Doe",
    "password": "securepassword123"
}
Response:
JSON

{
    "user": {
        "id": 1,
        "email": "user@example.com",
        "name": "John Doe"
    },
    "tokens": {
        "refresh": "refresh_token_here",
        "access": "access_token_here"
    },
    "message": "User registered successfully"
}
2. User Login
URL: /api/auth/login/
Method: POST
Body:
JSON

{
    "email": "user@example.com",
    "password": "securepassword123"
}
Response:
JSON

{
    "user": {
        "id": 1,
        "email": "user@example.com",
        "name": "John Doe"
    },
    "tokens": {
        "refresh": "refresh_token_here",
        "access": "access_token_here"
    },
    "message": "Login successful"
}
Patient Management Endpoints
1. Create Patient
URL: /api/patients/
Method: POST
Headers: Authorization: Bearer <access_token>
Body:
JSON

{
    "first_name": "Jane",
    "last_name": "Smith",
    "date_of_birth": "1990-01-01",
    "gender": "F",
    "phone_number": "1234567890",
    "email": "jane@example.com",
    "address": "123 Main St, City, Country",
    "medical_history": "No significant medical history"
}
2. List All Patients
URL: /api/patients/
Method: GET
Headers: Authorization: Bearer <access_token>
Response: Array of patient objects
3. Get Patient Details
URL: /api/patients/{id}/
Method: GET
Headers: Authorization: Bearer <access_token>
4. Update Patient
URL: /api/patients/{id}/
Method: PUT
Headers: Authorization: Bearer <access_token>
Body: Updated patient data
5. Delete Patient
URL: /api/patients/{id}/
Method: DELETE
Headers: Authorization: Bearer <access_token>
Doctor Management Endpoints
1. Create Doctor
URL: /api/doctors/
Method: POST
Headers: Authorization: Bearer <access_token>
Body:
JSON

{
    "first_name": "Robert",
    "last_name": "Johnson",
    "specialization": "Cardiology",
    "license_number": "LIC12345",
    "phone_number": "9876543210",
    "email": "dr.robert@example.com",
    "years_of_experience": 10
}
2. List All Doctors
URL: /api/doctors/
Method: GET
Headers: Authorization: Bearer <access_token>
3. Get Doctor Details
URL: /api/doctors/{id}/
Method: GET
Headers: Authorization: Bearer <access_token>
4. Update Doctor
URL: /api/doctors/{id}/
Method: PUT
Headers: Authorization: Bearer <access_token>
5. Delete Doctor
URL: /api/doctors/{id}/
Method: DELETE
Headers: Authorization: Bearer <access_token>
Patient-Doctor Mapping Endpoints
1. Create Mapping
URL: /api/mappings/
Method: POST
Headers: Authorization: Bearer <access_token>
Body:
JSON

{
    "patient": 1,
    "doctor": 1,
    "reason_for_visit": "Regular checkup"
}
2. List All Mappings
URL: /api/mappings/
Method: GET
Headers: Authorization: Bearer <access_token>
3. Get Doctors for a Patient
URL: /api/mappings/patient/{patient_id}/
Method: GET
Headers: Authorization: Bearer <access_token>
4. Delete Mapping
URL: /api/mappings/{id}/
Method: DELETE
Headers: Authorization: Bearer <access_token>
Database Schema
User Model
Field	Type	Description
id	Integer	Primary key
email	Email	Unique email address
name	String	User's full name
password	String	Encrypted password
is_active	Boolean	Account status
is_staff	Boolean	Staff status
created_at	DateTime	Account creation timestamp
updated_at	DateTime	Last update timestamp
Patient Model
Field	Type	Description
id	Integer	Primary key
user	ForeignKey	Reference to User
first_name	String	Patient's first name
last_name	String	Patient's last name
date_of_birth	Date	Birth date
gender	String	Gender (M/F/O)
phone_number	String	Contact number
email	Email	Email address
address	Text	Physical address
medical_history	Text	Medical history notes
created_at	DateTime	Record creation timestamp
updated_at	DateTime	Last update timestamp
Doctor Model
Field	Type	Description
id	Integer	Primary key
user	ForeignKey	Reference to User
first_name	String	Doctor's first name
last_name	String	Doctor's last name
specialization	String	Medical specialization
license_number	String	Medical license number
phone_number	String	Contact number
email	Email	Email address
years_of_experience	Integer	Experience in years
created_at	DateTime	Record creation timestamp
updated_at	DateTime	Last update timestamp
PatientDoctorMapping Model
Field	Type	Description
id	Integer	Primary key
patient	ForeignKey	Reference to Patient
doctor	ForeignKey	Reference to Doctor
assigned_by	ForeignKey	Reference to User
reason_for_visit	Text	Reason for assignment
created_at	DateTime	Mapping creation timestamp
updated_at	DateTime	Last update timestamp
Authentication
JWT Token Structure
The system uses JWT (JSON Web Tokens) for authentication:

Access Token: Short-lived token (60 minutes) for API access
Refresh Token: Long-lived token (7 days) for obtaining new access tokens
Using Tokens
Include the access token in the Authorization header:


Authorization: Bearer <access_token>
Token Refresh
When the access token expires, use the refresh token to get a new one:

BASH

POST /api/auth/token/refresh/
{
    "refresh": "refresh_token_here"
}
Testing
Using Postman
Import the API collection
Set up environment variables for tokens
Test each endpoint systematically
Using cURL
BASH

Collapse
# Register user
curl -X POST http://localhost:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{
    "email": "test@example.com",
    "name": "Test User",
    "password": "testpass123"
}'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{
    "email": "test@example.com",
    "password": "testpass123"
}'

# Create patient (with token)
curl -X POST http://localhost:8000/api/patients/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1985-05-15",
    "gender": "M",
    "phone_number": "5551234567",
    "email": "john.doe@example.com",
    "address": "456 Oak St, City, Country",
    "medical_history": "Hypertension"
}'
Unit Testing
Run Django tests:

BASH

python manage.py test
Deployment
Production Checklist
Set DEBUG = False in production# Health_Care
