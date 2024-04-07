import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 사용자 테이블과 계좌 테이블 생성
create_users_table = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
'''
cursor.execute(create_users_table)

create_accounts_table = '''
CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    balance REAL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);
'''

cursor.execute(create_accounts_table)

# 트랜잭션 예제


def transfer_money(from_user_id, to_user_id, amount):
    try:
        # 트랜잭션 시작
        cursor.execute("BEGIN")

        # 보내는 사용자의 계좌에서 금액 차감
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE user_id = ?", (amount, from_user_id))

        # 받는 사용자의 계좌에 금액 추가
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE user_id = ?", (amount, to_user_id))

        # 트랜잭션 커밋
        conn.commit()
        print("이체 완료")
    except sqlite3.Error as e:
        # 트랜잭션 롤백
        conn.rollback()
        print("이체 중 오류 발생: ", e)


# 샘플 데이터 삽입
cursor.execute(
    "INSERT INTO accounts (user_id, balance) VALUES (?, ?)", (1, 1000))
cursor.execute(
    "INSERT INTO accounts (user_id, balance) VALUES (?, ?)", (2, 500))
conn.commit()

# 트랜잭션 예제 실행
transfer_money(1, 2, 200)

# 계좌 잔액 확인
cursor.execute(
    "SELECT users.name, accounts.balance FROM users JOIN accounts ON users.id = accounts.user_id")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]}의 잔액: {row[1]}")

# 데이터베이스 연결 종료
conn.close()
