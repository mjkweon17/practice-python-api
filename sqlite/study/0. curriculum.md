## SQLite 핵심
1. SQLite 개요
   - 경량의 파일 기반 데이터베이스
   - 서버가 필요 없는 임베디드 데이터베이스
   - 단일 파일에 모든 데이터를 저장
   - 간편한 설정과 관리
   - 중소규모 애플리케이션에 적합
2. SQLite 설치 및 사용
   - Python에는 기본적으로 SQLite가 내장되어 있음
   - `import sqlite3`로 SQLite 모듈 불러오기
   - `sqlite3.connect('database.db')`로 데이터베이스 연결
   - 연결 객체의 `cursor()` 메서드로 커서 생성
   - 커서의 `execute()`로 SQL 쿼리 실행
   - 연결 객체의 `commit()`으로 변경 사항 저장
   - 사용 후 연결 객체의 `close()`로 연결 종료
3. 테이블 생성 및 스키마 정의
   - `CREATE TABLE` 문을 사용하여 테이블 생성
   - 각 열의 이름과 데이터 타입 지정
   - 기본 키, 외래 키, 제약 조건 등을 정의
   - SQLite는 동적 타입을 지원하여 데이터 타입이 유연함
4. CRUD 작업
   - `INSERT` 문으로 데이터 삽입
   - `SELECT` 문으로 데이터 조회
   - `UPDATE` 문으로 데이터 수정
   - `DELETE` 문으로 데이터 삭제
   - 기본적인 SQL 문법과 유사
5. 인덱싱과 쿼리 최적화
   - 인덱스를 사용하여 쿼리 성능 향상
   - `CREATE INDEX` 문으로 인덱스 생성
   - 적절한 인덱스를 사용하여 검색 속도 개선
   - 복잡한 쿼리의 경우 `EXPLAIN` 문으로 쿼리 실행 계획 확인
6. 트랜잭션 처리
   - 트랜잭션을 사용하여 데이터 무결성 보장
   - `BEGIN`, `COMMIT`, `ROLLBACK` 문으로 트랜잭션 제어
   - 충돌 해결을 위한 동시성 제어 메커니즘 제공
7. FastAPI와의 통합
   - SQLite 데이터베이스 연결 및 종속성 주입
   - FastAPI의 Pydantic 모델을 사용하여 데이터 유효성 검사
   - SQLAlchemy 등의 ORM을 활용하여 데이터베이스 작업 단순화
   - 요청 핸들러에서 데이터베이스 쿼리 실행
8. 데이터 백업 및 복원
   - SQLite 데이터베이스 파일 복사로 간단한 백업 가능
   - `sqlite3` 명령행 도구를 사용하여 데이터 덤프 및 복원
   - 정기적인 백업 수행으로 데이터 손실 예방
9. 제한 사항 및 고려 사항
   - 대용량 데이터나 높은 동시성 처리에는 적합하지 않을 수 있음
   - 복잡한 쿼리나 고급 SQL 기능은 제한적일 수 있음
   - 데이터 무결성과 일관성을 위해 적절한 제약 조건 설정 필요
   - 백업 및 복제 전략 수립 필요
10. 추가 리소스
    - SQLite 공식 문서 참조: https://www.sqlite.org/docs.html
    - Python SQLite3 모듈 문서 참조: https://docs.python.org/3/library/sqlite3.html
    - FastAPI 공식 문서의 데이터베이스 관련 섹션 참조: https://fastapi.tiangolo.com/tutorial/sql-databases/