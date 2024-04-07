import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

drop_table_query = 'DROP TABLE IF EXISTS books'

try:
    cursor.execute(drop_table_query)
    conn.commit()
    print("테이블이 성공적으로 삭제되었습니다.")
except sqlite3.Error as e:
    print("테이블 삭제 중 오류가 발생했습니다: ", e)
finally:
    cursor.close()
    conn.close()
