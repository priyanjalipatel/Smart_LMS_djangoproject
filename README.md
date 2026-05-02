# 📚 Smart LMS – Stage 1 (Django Project)

## 🚀 Project Overview

Smart LMS (Learning Management System) is a beginner-friendly Django web application that allows users to browse courses, view details, and register/login. This project demonstrates core Django concepts including authentication, database models, form handling, and media file uploads.

---

## 🎯 Features Implemented (Stage 1)

### 🔐 Authentication System

* User Registration
* Login / Logout
* Password hashing (secure storage)
* Session management
* Form validation (username, password, email)

---

### 📘 Course Management

* Course listing page
* Course detail page
* Admin panel for managing courses
* Upload course thumbnails (images)

---

### 🖼️ Media Handling

* Image uploads stored in `/media/`
* Uses Pillow for image processing
* Dynamic rendering of uploaded images

---

### 🎨 Frontend

* Django templates (HTML)
* Base template with reusable layout
* Responsive UI structure

---

## 🏗️ Project Structure

```
mks11_smart_lms_stage1/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── media/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── apps/
│   └── courses/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── forms.py
│       ├── admin.py
│
├── templates/
│   └── courses/
│       ├── base.html
│       ├── home.html
│       ├── course_list.html
│       ├── course_detail.html
│       ├── login.html
│       ├── register.html
│
└── static/
    └── css/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-link>
cd mks11_smart_lms_stage1
```

---

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create superuser

```
python manage.py createsuperuser
```

---

### 6. Run development server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔧 Key Concepts Used

* Django MVT Architecture (Model – View – Template)
* ORM (Object Relational Mapping)
* Form validation system
* Built-in authentication
* Media file handling
* Admin panel customization

---

## 🔄 Application Flow

1. User visits homepage
2. Views featured courses
3. Navigates to course list or detail
4. Registers account
5. Gets logged in automatically
6. Accesses protected features

---

## 📷 Media Configuration

Ensure the following in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

And in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧪 Admin Panel

Access:

```
http://127.0.0.1:8000/admin/
```

* Add/Edit/Delete courses
* Upload course images
* Manage users

---

## 🚧 Future Enhancements (Stage 2+)

* 🎥 Video lecture integration
* 👨‍🎓 Role-based dashboards (Student / Instructor / Admin)
* 💳 Payment gateway integration
* 📊 Progress tracking & analytics
* 🔒 Digital Rights Management (DRM)

---

## 🧠 Learning Outcomes

By completing this project, you understand:

* How Django projects are structured
* How backend connects to frontend
* How authentication works internally
* How databases interact with web apps

---

## 📌 Notes

* This is a **Stage 1 (beginner-level)** project
* Focus is on understanding Django fundamentals
* Code is modular and extendable for future stages

---

## 🙌 Acknowledgment

Built as part of a hands-on learning journey in Django and web development.

---
