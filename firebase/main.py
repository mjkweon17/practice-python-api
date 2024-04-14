from fastapi import FastAPI
from .auth.router import router as auth_router
import firebase_auth

app = FastAPI()
app.include_router(auth_router)
