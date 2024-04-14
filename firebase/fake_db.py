from typing import List, Dict
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


fake_db: List[User] = [
    User(id=1, name="John Doe", email="john@kucc.com"),
    User(id=2, name="mj", email="mj@kucc.com"),
    User(id=3, name="jane", email="jane@kucc.com"),
    User(id=4, name="sb", email="sb@kucc.com")
]


async def get_db() -> List[User]:
    return fake_db


async def get_user_by_id(user_id: int) -> User:
    for user in fake_db:
        if user.id == user_id:
            return user
    raise ValueError(f"User with ID {user_id} not found")


async def create_user(user: User) -> User:
    fake_db.append(user)
    return user


async def update_user(user_id: int, updated_user: User) -> User:
    for i, user in enumerate(fake_db):
        if user.id == user_id:
            fake_db[i] == updated_user
            return updated_user
    raise ValueError(f"User with ID {user_id} not found")


async def delete_user(user_id: int):
    for i, user in enumerate(fake_db):
        if user.id == user_id:
            del fake_db[i]
            return
    raise ValueError(f"User with ID {user_id} not found")
