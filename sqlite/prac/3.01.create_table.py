import sqlite3

# SQLite 데이터베이스 파일에 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()  # 커서는 데이터베이스에 SQL 쿼리를 실행하고 결과를 가져오는데 사용됨.

# users 테이블 생성
create_table_query = '''
CREATE TABLE IF NOT EXiSTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
);
'''

cursor.execute(create_table_query)

# 변경 사항 커밋
conn.commit()

# 데이터베이스 연결 종료
conn.close()


'''
conn.commit()과 conn.close()를 호출하지 않아도 테이블 생성은 이루어짐. 하지만 데이터베이스 연결을 명시적으로 커밋하고 닫는 것이 좋음.

conn.commit()을 호출하지 않으면 변경 사항이 데이터베이스에 즉시 반영되지 않을 수 있음.
SQLite는 기본적으로 자동 커밋 모드로 동작하지만, 명시적으로 conn.commit()을 호출하여 변경 사항을 확실히 저장하는 것이 안전

conn.close()를 호출하지 않으면 데이터베이스 연결이 계속 열려 있게 됨. 이는 리소스 누구(resouce leak)를 야기할 수 있으며, 다른 프로세스나 스레드에서 데이터베이스 파일에 접근하는 것을 방해할 수 있음. 따라서 데이터베이스 작업이 완료되면 conn.close()를 호출하여 연결을 닫는 것이 좋음.
'''
