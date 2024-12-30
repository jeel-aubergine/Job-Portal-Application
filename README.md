# Job Portal Application

A Django-based web application that allows users to manage job postings. This project includes functionalities for user authentication, company registration, and job management.

## Features
- User Authentication (Sign Up, Login, Logout)
- Company Registration and Management
- Job Posting Creation, Editing, and Deletion
- Paginated Job Listings

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.10+
- pip
- Virtual Enviroments
- Git

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jeel-aubergine/Job-Portal-Application.git
cd job_portal
```

### 2. Create and Activate Virtual Environment (Optional)

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

By default, the project uses SQLite. To use the default configuration:

```bash
python manage.py makemigrations
python manage.py migrate
```

If you'd like to use a different database, update `DATABASES` in `job_portal/settings.py` and apply migrations.

### 5. Create a Superuser

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the server to test the application locally:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

## Key Functionalities

### User Authentication
- Sign up and log in using Django's built-in authentication system.
- Logout functionality to terminate sessions.

### Company Management
- Each user can register only one company.
- Companies are linked to the user.

### Job Management
- Jobs are associated with a registered company.
- Only the company owner can create, edit, or delete jobs.
- Job listings are paginated for better readability.

---

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/) for styling (optional).
