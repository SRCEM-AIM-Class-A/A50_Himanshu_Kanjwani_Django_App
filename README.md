# Django Multi-App Project

## Overview
A Django project with four independent apps, each serving its own webpage. This demonstrates Django's modular architecture.

## Requirements
- Python 3.8+
- Django 4.0+
- pip

## Setup
1. Clone repository:
```b
git clone https://github.com/SRCEM-AIM-Class-A/A50_Himanshu_Kanjwani_Django_App.git
cd StudentProject
```

2. Create and activate virtual environment:
```
python -m venv venv

# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Start development server:
```
python manage.py runserver
```

## App Endpoints
- App1: `http://localhost:8000/app1_home/` - App for Home Page; routes to home.html
- App2: `http://localhost:8000/app2_about/` - App for About Page; routes to about.html
- App3: `http://localhost:8000/app3_services/` - App for Services Page; routes to servives.html
- App4: `http://localhost:8000/app4_contacts/` - App for Contacts Page; routes to contacts.html

## Project Structure
```
StudentProject/
├── app1_home/         # Home app
│   ├── views.py       # Business logic
│   ├── urls.py        # URL routing
|   └── ...
├── app2_about/        # About app
├── app3_services/     # Services app
├── app4_contacts/     # Contacts app
├── StudentProject/    # Main config
│   ├── settings.py    # Project settings
│   ├── urls.py        # Main URLs
|   └── ...
├── templates/         # HTML templates
├── static/            # static files (CSS/JS)        
└── manage.py          # Django CLI
```
