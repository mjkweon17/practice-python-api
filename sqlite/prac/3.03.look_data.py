import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 데이터 조회
select_query = 'SELECT * FROM users;'
cursor.execute(select_query)
rows = cursor.fetchall()

# 조회 결과 출력
for row in rows:
    print(row)

conn.close()
