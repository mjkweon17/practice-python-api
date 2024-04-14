from pydantic import BaseModel


class LoginRequest(BaseModel):
    token: str


class SignupRequest(BaseModel):
    token: str
    password: str


class User(BaseModel):
    email: str
    # Add other user fields as needed


class Token(BaseModel):
    access_token: str
    token_type: str
