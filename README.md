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
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
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

## Usage Instructions

### 1. User Authentication
- Navigate to `/user/signup/` to create a new account.
- Login at `/user/login/`.

### 2. Company Registration
- After logging in, navigate to `/company/register/` to register your company.

### 3. Job Management
- Create jobs at `/job/create/`.
- View and manage jobs at `/job/list/`.
  - Edit jobs by clicking on the "Edit" link.
  - Delete jobs by clicking on the "Delete" link.

### 4. Admin Panel
Access the Django admin panel at `/admin/` to manage users, companies, and jobs directly.

---

## Project Structure

```plaintext
job_portal/
├── job_portal/         # Project-level settings and URLs
├── user/               # User authentication app
├── company/            # Company management app
├── job/                # Job management app
├── templates/          # HTML templates for the app 
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

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
