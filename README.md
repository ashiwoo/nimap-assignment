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
-----
```
### screenshorts
![WhatsApp Image 2025-07-20 at 5 35 17 PM](https://github.com/user-attachments/assets/72ec5013-6ff7-40b0-bd44-fb7c4d481307)
![WhatsApp Image 2025-07-20 at 5 34 20 PM](https://github.com/user-attachments/assets/f557af6f-24b3-41f5-b7c8-0e3d97ddfd05)
![WhatsApp Image 2025-07-20 at 5 48 36 PM](https://github.com/user-attachments/assets/3e8857ef-21a4-4bca-9706-8b93f944b5f3)
![WhatsApp Image 2025-07-20 at 6 16 22 PM](https://github.com/user-attachments/assets/2441cd0d-0977-439c-8124-acf0658e3e86)
![WhatsApp Image 2025-07-20 at 7 05 14 PM](https://github.com/user-attachments/assets/6f582b7c-2f3f-4629-8ab1-0f744b871f6e)
![WhatsApp Image 2025-07-20 at 7 07 39 PM](https://github.com/user-attachments/assets/e42cec3f-ffb6-4cc0-8580-353cd8ccdf54)
![WhatsApp Image 2025-07-20 at 7 15 24 PM](https://github.com/user-attachments/assets/8f470c2d-b806-4a81-a85b-f56b9e9f997f)







