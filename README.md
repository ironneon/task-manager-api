# Task Manager API

A RESTful Task Manager API built with **FastAPI** and **PostgreSQL**, featuring user authentication and secure task management.

## Features

- User registration and login
- Secure password hashing with Argon2
- JWT authentication
- Create, read, update, and delete tasks
- User-specific task management
- Protected API endpoints
- PostgreSQL database integration

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- PyJWT
- pwdlib (Argon2)
- Uvicorn

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ironneon/task-manager-api.git
cd task-manager-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=task_manager_db
SECRET_KEY=your_secret_key
```

Never commit your `.env` file or share your secret key.

### 6. Run the application

```bash
uvicorn main:app --reload
```

## API Documentation

Once the server is running, open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Authentication

Register a new user using:

```http
POST /register
```

Log in using:

```http
POST /login
```

Use the returned JWT access token to authorize protected endpoints.

## Task Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Get your tasks |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Update your task |
| DELETE | `/tasks/{task_id}` | Delete your task |

## Security

- Passwords are hashed before storage.
- Protected endpoints require a valid JWT token.
- Users can only access their own tasks.
- Unauthorized requests are rejected.

## Author

**ironneon**

GitHub: https://github.com/ironneon

