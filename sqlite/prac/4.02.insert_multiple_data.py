import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 여러 행 삽입
insert_query = "INSERT INTO users (name, email, age) VALUES(?, ?, ?)"
data = [
    ('호진', 'hhj@gmail.com', 21),
    ('유한', 'pyh@gmail.com', 21)
]

cursor.executemany(insert_query, data)

conn.commit()
conn.close()

"""
아니요, `?`를 사용하여 매개변수를 바인딩하는 것은 SQLite뿐만 아니라 다른 데이터베이스에서도 사용되는 일반적인 기술입니다. 이를 준비된 문(Prepared Statement) 또는 매개변수화된 쿼리(Parameterized Query)라고 합니다.

준비된 문은 SQL 인젝션 공격을 방지하고 성능을 향상시키는 데 도움이 됩니다. 매개변수 자리에 `?`를 사용하고 실제 값은 별도로 전달함으로써, SQL 문과 데이터를 분리할 수 있습니다.

다른 데이터베이스에서도 유사한 방식을 사용할 수 있습니다. 예를 들어:

1. MySQL (mysql-connector-python):
```python
import mysql.connector

conn = mysql.connector.connect(...)
cursor = conn.cursor()

insert_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
data = [('호진', 'hhj@gmail.com', 21), ('유한', 'pyh@gmail.com', 21)]
cursor.executemany(insert_query, data)

conn.commit()
conn.close()
```

2. PostgreSQL (psycopg2):
```python
import psycopg2

conn = psycopg2.connect(...)
cursor = conn.cursor()

insert_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
data = [('호진', 'hhj@gmail.com', 21), ('유한', 'pyh@gmail.com', 21)]
cursor.executemany(insert_query, data)

conn.commit()
conn.close()
```

위의 예시에서 MySQL과 PostgreSQL은 `%s`를 사용하여 매개변수를 표시하고 있습니다.

따라서 `?`를 사용한 매개변수 바인딩은 SQLite 고유의 기능이 아니라 여러 데이터베이스에서 공통적으로 사용되는 기술입니다. 각 데이터베이스마다 매개변수를 표시하는 방식에 약간의 차이가 있을 수 있지만, 기본 개념은 동일합니다.
"""


"""
SQL 인젝션을 방지하는 데 준비된 문(Prepared Statement) 또는 매개변수화된 쿼리(Parameterized Query)가 도움이 되는 이유는 다음과 같습니다:

1. SQL 문과 데이터의 분리:
   - 준비된 문을 사용하면 SQL 문과 실제 데이터를 분리할 수 있습니다.
   - SQL 문에서 매개변수 자리에 `?` 또는 `%s`와 같은 플레이스홀더를 사용하고, 실제 데이터는 별도로 전달합니다.
   - 이렇게 하면 사용자 입력이 SQL 문의 구조를 변경할 수 없게 됩니다.

2. 자동 이스케이프 처리:
   - 준비된 문을 사용할 때 데이터베이스 드라이버나 라이브러리는 자동으로 특수 문자를 이스케이프 처리합니다.
   - 사용자 입력에 포함된 작은따옴표(`'`), 큰따옴표(`"`), 백슬래시(`\`) 등의 특수 문자가 올바르게 처리되어 SQL 인젝션 공격을 방지할 수 있습니다.

3. 사용자 입력 값 검증:
   - 준비된 문을 사용하면 사용자 입력 값이 SQL 문의 일부로 처리되는 것이 아니라 별도의 데이터로 전달됩니다.
   - 이를 통해 사용자 입력 값을 검증하고 필터링하는 과정을 거칠 수 있습니다.
   - 입력 값의 유효성을 검사하고 유해한 문자나 패턴을 제거할 수 있습니다.

4. 성능 향상:
   - 준비된 문은 한 번 파싱되고 컴파일된 후 여러 번 실행될 수 있습니다.
   - 데이터베이스는 준비된 문을 캐시하고 재사용할 수 있어 반복적인 쿼리 실행 시 성능이 향상됩니다.

예를 들어, 다음과 같은 안전하지 않은 코드가 있다고 가정해보겠습니다:

```python
name = input("Enter your name: ")
query = f"SELECT * FROM users WHERE name = '{name}'"
cursor.execute(query)
```

위 코드에서는 사용자 입력을 직접 SQL 문자열에 삽입하고 있습니다. 만약 사용자가 악의적인 입력을 제공하면 SQL 인젝션 공격이 발생할 수 있습니다.

하지만 준비된 문을 사용하면 다음과 같이 안전하게 코드를 작성할 수 있습니다:

```python
name = input("Enter your name: ")
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (name,))
```

이렇게 하면 사용자 입력이 SQL 문과 분리되어 전달되므로 SQL 인젝션 공격을 방지할 수 있습니다.

준비된 문을 사용하는 것은 SQL 인젝션을 방지하는 효과적인 방법 중 하나이며, 안전하고 견고한 데이터베이스 프로그래밍을 위해 권장되는 방식입니다.
"""
