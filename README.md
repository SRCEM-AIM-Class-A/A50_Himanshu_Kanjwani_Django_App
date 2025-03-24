```
# Django Multi-App Project

## Overview
A Django project with four independent apps, each serving its own webpage. This demonstrates Django's modular architecture.

## Requirements
- Python 3.8+
- Django 4.0+
- pip

## Setup
1. Clone repository:
```bash
git clone https://github.com/yourusername/projectname.git
cd projectname
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start development server:
```bash
python manage.py runserver
```

## App Endpoints
- App1: `http://localhost:8000/app1/` - [Brief description]
- App2: `http://localhost:8000/app2/` - [Brief description]
- App3: `http://localhost:8000/app3/` - [Brief description]
- App4: `http://localhost:8000/app4/` - [Brief description]

## Project Structure
```
project_root/
├── app1/              # First app
│   ├── views.py       # Business logic
│   ├── urls.py        # URL routing
│   └── templates/     # HTML templates
├── app2/              # Second app
├── app3/              # Third app
├── app4/              # Fourth app
├── project_name/      # Main config
│   ├── settings.py    # Project settings
│   └── urls.py        # Main URLs
└── manage.py          # Django CLI
```
