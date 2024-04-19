1. github actions로 ssh 접속을 테스트한다
2. github actions로 container registry 접속을 테스트한다
3. github actions로 배포 테스트를 해본다
4. github actions로 


1. Connection Method가 Standard (TCP/IP)와 Standard TCP/IP Over SSH일 때의 차이
2. SSH Tunneling의 구체적인 원리
3. 구현 방법
4. 테스트


1. 코드를 통한 접속
    - database.py를 열심히 수정해본다
    - ssh 접속을 하는 무슨 코드를 추가하고,,, (이미 수빈이가 함) database.py 코드를 열심히 수정해본다
2. 코드를 사용하지 않고 문제 해결
    - 로컬에서 FastAPI를 실행했을 때 서버 내에서 실행한 것과 같은 환경에서 실행되도록 해준다
        - 컴퓨터 자체 설정 변경 또는 네트워크 설정 변경 또는 vscode 같은 ide 설정 변경...?
    - 카카오 클라우드에서 ssh tunneling을 하지 않아도 되도록 설정을 변경해준다
        - vpc 설정을 변경해준다
        - mysql 설정을 변경해준다...