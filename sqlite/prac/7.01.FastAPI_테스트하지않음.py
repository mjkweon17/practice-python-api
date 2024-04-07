from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# SQLite 데이터베이스 연결
def get_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
    ''')
    conn.commit()
    try:
        yield conn
    finally:
        conn.close()

# Pydantic 모델 정의
class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

# 사용자 생성 API
@app.post("/users", response_model=User)
def create_user(user: UserCreate, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (user.name, user.email, user.age))
        user_id = cursor.lastrowid
        db.commit()
        return {"id": user_id, "name": user.name, "email": user.email, "age": user.age}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists")

# 사용자 조회 API
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        return {"id": user[0], "name": user[1], "email": user[2], "age": user[3]}
    else:
        raise HTTPException(status_code=404, detail="User not found")

# 사용자 삭제 API
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    db.commit()
    return {"message": "User deleted successfully"}