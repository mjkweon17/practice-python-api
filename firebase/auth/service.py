from sqlalchemy.orm import Session
from . import models


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, email: str, password: str):
    new_user = models.User(email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_access_token(data: dict):
    # Use a JWT library to create and return an access token
    # Example using PyJWT:
    # import jwt
    # access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    # return access_token
    pass
