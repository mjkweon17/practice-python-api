from sqlalchemy.orm import Session
from firebase_admin import auth

from .database import SessionLocal
from .firebase import firebase_auth


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_firebase_auth():
    return auth
