# Marketing Agency Management Backend

This is the backend repository for an all-in-one management tool for a marketing agency. The project is a full-stack solution where the backend and frontend communicate via a REST API.

### Key Technologies

- **Backend:** **Django** and **Django REST Framework** for creating a robust RESTful API.
- **Dashboard Frontend:** **React** for a dynamic and modern user interface.
- **Authentication:** Implementation of a user authentication system for secure access to the dashboard.

### Core Features

- **Administrative Dashboard:** An intuitive interface for the agency's team to manage clients, campaigns, and reports.
- **RESTful API:** A set of endpoints to efficiently interact with the database.
- **Security:** A login and session management system to protect sensitive information.

### Getting Started

To clone and run the project, follow these steps:

## 1. Clone the repository

```bash
  git clone https://github.com/fernandojosemoran/marketing-agency-backend.git && cd marketing-agency-backend
```

## 2. Create a django environment

```bash
  # windows
  python -m venv .venv && .\.venv\Scripts\Activate

  # linux
  python3 -m venv .venv && source .venv/bin/activate
```

## 3. Install Django dependencies:

```bash
  # linux
  pip3 install -r requirements.txt

  # windows
  pip install -r requirements.txt
```

## 4. Configure the environment variables

Open your .env file with your text reader favorite.

```bash
  # windows
  notepad ./core/.env

  # linux
  nano ./core/.env
```

```.env
SECRET_KEY="" # If you don't have a SECRET_KEY for Django, you can generate a random one here: https://djecrety.ir/
DEBUG=True # If you want to deploy the backend in production, switch the DEBUG variable to False
CORST_ORIGIN_WHITELIST_DEPLOY="localhost,127.0.0.1"
DATABASE_URL="" # Optional
DOMAIN_DEV="localhost,127.0.0.1"
DOMAIN_PRODUCTION="localhost,127.0.0.1"

ALLOWED_HOSTS_DEV="localhost,127.0.0.1"
ALLOWED_HOSTS_DEPLOY="localhost,127.0.0.1"
CSRF_TRUSTED_ORIGINS_DEV="http://localhost,[http://127.0.0.1](http://127.0.0.1)"
CSRF_TRUSTED_ORIGINS_DEPLOY="http://localhost,[http://127.0.0.1](http://127.0.0.1)"

POSTGRES_DB= # the database should exist before you run the backend
POSTGRES_USER=postgres
POSTGRES_PASSWORD=
POSTGRES_PORT=5434
POSTGRES_HOST=127.0.0.1 # If your database is in the cloud, type the URL of your provider.

## Bucket for saving images
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=

# You can select between S3 and Local options to tell Django how to save images
# If you select LOCAL, images will be saved in the media folder when you create a post.
STORAGE_DESTINATION=LOCAL

# STORAGE_DESTINATION=S3
```

## 5 Installing the react packages

```bash
  npm install && npm build
```

## 6 Run the backend

```bash
  npm install && npm run build
```

```bash
  # windows
  python .\manage.py runserver 80 # Or any other port you prefer

  # linux
  python3 ./manage.py runserver 80 # Or any other port you prefer
```

```bash
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified some issues:

  System check identified 1 issue (0 silenced).
  July 31, 2025 - 00:41:05
  Django version 5.2.4, using settings 'core.settings'
  Starting development server at http://127.0.0.1:80/
  Quit the server with CTRL-BREAK.
```
