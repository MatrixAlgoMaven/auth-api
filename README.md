# Auth API

A REST API built with **FastAPI** and **Supabase Auth** that supports user signup, login, logout, and protected endpoints using Bearer token authentication.

## Features

* User registration with Supabase Auth
* Login with email and password
* Access and refresh token responses
* Protected profile and dashboard endpoints
* Token verification through Supabase
* Logout endpoint
* Public information endpoint
* Swagger UI with Bearer authentication

## Tech Stack

* Python
* FastAPI
* Supabase
* Uvicorn
* HTTPX
* python-dotenv

## Requirements

* Python 3.10 or newer
* A Supabase project
* Git

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/MatrixAlgoMaven/auth-api.git
cd auth-api
```


### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create your local `.env` file using `.env.example` as a template.

Set your own Supabase project URL and anon/publishable key in `.env`. Never commit real credentials to GitHub.

### 5. Run the API

```bash
uvicorn main:app --reload --port 8000
```

Open the interactive API documentation at:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint               | Description                          |
| ------ | ---------------------- | ------------------------------------ |
| POST   | `/auth/signup`         | Register a user                      |
| POST   | `/auth/login`          | Log in and receive tokens            |
| POST   | `/auth/logout`         | Log out the authenticated session    |
| GET    | `/public/info`         | Public information                   |
| GET    | `/protected/profile`   | Get the authenticated user's profile |
| GET    | `/protected/dashboard` | Access the protected dashboard       |

## Authentication

Protected routes require a valid Supabase access token in the Bearer authorization header.

In Swagger UI:

1. Log in using `/auth/login`.
2. Copy the `access_token` from the response.
3. Click **Authorize**.
4. Enter the access token and authorize.
5. Execute a protected endpoint.

## Security Notes

* Keep `.env` private and out of version control.
* Use `.env.example` as a template only.
* Never publish passwords, access tokens, refresh tokens, or service-role keys.
* An access token may remain valid until it expires, even after logout.

## License

No license has been specified yet.
