import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
PORT = int(os.getenv("PORT", "8000"))

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()


class AuthRequest(BaseModel):
    email: str | None = None
    password: str | None = None


@app.get("/")
def root():
    return {"message": "Server running and connected to Supabase"}


@app.post("/auth/signup", status_code=201)
def signup(request: AuthRequest):
    if not request.email or not request.password:
        return JSONResponse(
            status_code=400,
            content={"error": "Email and password are required"}
        )

    try:
        response = supabase.auth.sign_up({
            "email": request.email,
            "password": request.password
        })

        return {
            "user": response.user.model_dump() if response.user else None
        }

    except Exception as e:
        error_message = str(e)

        if "rate limit" in error_message.lower():
            return JSONResponse(
                status_code=429,
                content={"error": "Email rate limit exceeded. Please try again later."}
            )

        return JSONResponse(
            status_code=400,
            content={"error": error_message}
        )

@app.post("/auth/login")
def login(request: AuthRequest):
    if not request.email or not request.password:
        return JSONResponse(
            status_code=400,
            content={"error": "Email and password are required"}
        )

    try:
        response = supabase.auth.sign_in_with_password({
            "email": request.email,
            "password": request.password
        })

        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }

    except Exception:
        return JSONResponse(
            status_code=401,
            content={"error": "Invalid login credentials"}
        )