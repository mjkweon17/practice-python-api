import sqlite3
import time
import random

# SQLite 데이터베이스 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# books 테이블 생성
create_table_query = '''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT UNIQUE,
    published_year INTEGER
);
'''
cursor.execute(create_table_query)

# 대량의 샘플 데이터 생성
data = []
for i in range(1, 1000001):
    title = f"book {i}"
    content = f"this is content of book {i}"
    published_year = random.randint(1970, 2024)
    data.append((title, content, published_year))

# 데이터 삽입
insert_query = "INSERT INTO books (title, content, published_year) VALUES (?, ?, ?)"
cursor.executemany(insert_query, data)
conn.commit()

# 인덱스 생성 전 쿼리 실행 시간 측정
start_time = time.time()
select_query = "SELECT * FROM books WHERE content = ?"
cursor.execute(select_query, ("this is content of book 2024", ))
row = cursor.fetchone()
print("인덱스 없이 조회된 행: ", row)
end_time = time.time()
print("인덱스 없이 쿼리 실행 시간: ", end_time - start_time)

# content 열에 인덱스 생성
create_index_query = "CREATE INDEX idx_books_content ON books (content)"
cursor.execute(create_index_query)

# 인덱스 생성 후 쿼리 실행 시간 측정
start_time = time.time()
select_query = "SELECT * FROM books WHERE content = ?"
cursor.execute(select_query, ("this is content of book 2024", ))
row = cursor.fetchone()
print("인덱스로 조회된 행: ", row)
end_time = time.time()
print("인덱스로 쿼리 실행 시간: ", end_time - start_time)

# 데이터베이스 연결 종료
conn.close()

"""
인덱스 없이: 0.0010073184967041016
인덱스 있이: 0.0010013580322265625
0.000006초 정도 빨라진 것을 볼 수 있다!

INT인 published_year로 했을 때는 차이가 없었다. 없을 것 같긴하다...
"""

'''
`cursor.execute()` 메서드에 매개변수를 전달할 때 `('user50000@example.com',)`와 같이 괄호로 감싸고 쉼표를 추가한 이유는 튜플(tuple)로 매개변수를 전달하기 위해서입니다.

`cursor.execute()` 메서드는 SQL 쿼리와 매개변수를 받아서 실행합니다. 매개변수는 튜플이나 리스트 형태로 전달해야 합니다. 괄호로 감싸고 쉼표를 추가하는 이유는 다음과 같습니다:

1. 튜플로 매개변수 전달:
   - `cursor.execute()`에 매개변수를 전달할 때는 튜플 형태로 전달하는 것이 일반적입니다.
   - 튜플은 불변(immutable)하며, SQL 인젝션을 방지하는 데 도움이 됩니다.
   - `('user50000@example.com',)`와 같이 괄호로 감싸고 쉼표를 추가하면 튜플로 인식됩니다.

2. 단일 매개변수 전달:
   - SQL 쿼리에서 `?` 플레이스홀더가 하나만 사용되었기 때문에 단일 매개변수를 전달해야 합니다.
   - 단일 매개변수를 전달할 때도 튜플 형태로 전달해야 합니다.
   - `('user50000@example.com',)`와 같이 괄호로 감싸고 쉼표를 추가하면 튜플로 인식되어 단일 매개변수로 처리됩니다.

만약 괄호와 쉼표를 생략하고 `'user50000@example.com'`만 전달하면, 문자열로 인식되어 에러가 발생할 수 있습니다. 튜플로 전달해야 `cursor.execute()`에서 매개변수를 올바르게 인식하고 처리할 수 있습니다.

따라서 `('user50000@example.com',)`와 같이 괄호로 감싸고 쉼표를 추가하는 이유는 단일 매개변수를 튜플 형태로 전달하기 위한 것입니다.

참고로 여러 개의 매개변수를 전달할 때는 `(param1, param2, ...)`와 같이 쉼표로 구분하여 튜플로 전달하면 됩니다.
'''
