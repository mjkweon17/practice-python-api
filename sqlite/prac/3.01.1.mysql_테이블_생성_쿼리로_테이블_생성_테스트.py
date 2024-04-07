import sqlite3

# SQLite 데이터베이스 파일에 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()  # 커서는 데이터베이스에 SQL 쿼리를 실행하고 결과를 가져오는데 사용됨.

# users 테이블 생성
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  age INT
);
'''
# 잘 작동함. ㄷㄷㄷㄷ

cursor.execute(create_table_query)

# 변경 사항 커밋
conn.commit()

# 데이터베이스 연결 종료
conn.close()


'''
SQLite는 데이터 타입에 대해 좀 더 유연한 접근 방식을 가지고 있기 때문에, MySQL 문법으로 작성된 쿼리가 SQLite에서도 잘 작동할 수 있습니다.

SQLite에서는 데이터 타입이 엄격하게 enforced되지 않으며, 컬럼의 데이터 타입은 값에 따라 동적으로 결정됩니다. 따라서 MySQL에서 사용되는 INT, VARCHAR, AUTO_INCREMENT와 같은 데이터 타입과 키워드가 SQLite에서도 인식되고 허용됩니다.

위의 쿼리를 SQLite에서 실행했을 때 잘 작동하는 이유는 다음과 같습니다:

INT는 SQLite에서 INTEGER로 인식됩니다.
VARCHAR(255)는 SQLite에서 TEXT로 취급됩니다. SQLite는 문자열의 최대 길이를 지정하는 것을 무시합니다.
AUTO_INCREMENT는 SQLite에서 AUTOINCREMENT로 해석됩니다.
PRIMARY KEY와 UNIQUE 제약 조건은 SQLite에서도 동일하게 작동합니다.
따라서 위의 MySQL 문법으로 작성된 쿼리가 SQLite에서도 정상적으로 실행되고 테이블이 생성됩니다.

하지만 SQLite와 MySQL은 서로 다른 데이터베이스 시스템이므로, 일부 기능이나 문법에서 차이가 있을 수 있습니다. 특정 기능을 사용할 때는 해당 데이터베이스 시스템의 문서를 참조하여 정확한 문법과 지원 여부를 확인하는 것이 좋습니다.


'''
