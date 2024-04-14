from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from firebase_admin import auth as firebase_auth

import fake_db as db
from auth import schemas, service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/users")
async def list_users():
    users = await service.get_all_users()
    return users
