from fastapi import FastAPI
from auth.router import router as auth_router
import firebase_auth

from firebase_admin import auth

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Firebase SDK 테스트"}
