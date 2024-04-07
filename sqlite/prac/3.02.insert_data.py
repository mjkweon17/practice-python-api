import sqlite3

# SQLite 데이터베이스 파일에 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 데이터 삽입
insert_data_query = '''
INSERT INTO users (name, email, age) VALUES
    (민재', 'minjae@gmail.com', 29),
    ('지수', 'hjs@gmail.com', 25),
    ('희철', 'rhc@gmail.com', '25'),
    ('병현', 'byunghyun@gmail.com', 25);
'''
cursor.execute(insert_data_query)

# 변경 사항 커밋
conn.commit()

# 데이터베이스 연결 종료
conn.close()
