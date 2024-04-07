import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 단일 행 삽입
insert_query = "INSERT INTO users(name, email, age) VALUES (?, ?, ?)"
cursor.execute(insert_query, ('광영', 'lgy@gmail.com', 21))

conn.commit()
conn.close()
