# Nimap Company Management System – Assignment

This is a Django-based REST API project developed as part of the assignment for **Nimap Infotech**. It manages **Users**, **Clients**, and **Projects**, with token-based authentication and user-specific project access.

---

## 🚀 Features

- User Authentication via Token
- CRUD APIs for:
  - Clients
  - Projects
- Assigning Projects to Users
- Fetching Projects Assigned to a User
- Clean separation of concerns via Django and DRF best practices

---

## 📦 Tech Stack

- Python 3.x
- Django
- Django REST Framework (DRF)
- MySQL
- Token Authentication (DRF)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ashiwoo/nimap-assignment.git
cd nimap-assignment

### 2. Set Up Virtual Environment
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 5. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 6. Create a Superuser
python manage.py createsuperuser

### 7. Run the Development Server
python manage.py runserver
Server will be available at:
http://127.0.0.1:8000

🔐 Authentication
Generate Token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.get(username='your_username')
token, _ = Token.objects.get_or_create(user=user)
print(token.key)
Use in Postman or curl:
Authorization: Token your_token_here
Test the API (Example)
curl -H "Authorization: Token your_token_here" http://127.0.0.1:8000/api/projects/

OR in Postman:
Select GET
URL: http://127.0.0.1:8000/api/projects/
Header: Authorization: Token your_token_here

🗂️ Project Structure
nimap_company_management_system/
├── nimap_project/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md

