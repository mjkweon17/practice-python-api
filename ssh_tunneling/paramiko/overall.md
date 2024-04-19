https://www.paramiko.org/

https://velog.io/@engineer_km/paramiko

# paramiko

`paramiko`는 Python에서 사용할 수 있는 SSH2 프로토콜 라이브러리입니다. 이 라이브러리를 사용하면 Python 코드에서 SSH 클라이언트와 서버 기능을 구현할 수 있습니다. 주요 기능은 다음과 같습니다:

1. **SSH 연결 및 인증**: `paramiko`를 사용하면 SSH 서버에 연결하고 사용자 이름과 비밀번호 또는 SSH 키를 사용하여 인증할 수 있습니다.

2. **원격 명령 실행**: `paramiko`를 사용하면 원격 SSH 서버에서 명령을 실행하고 출력을 가져올 수 있습니다.

3. **SFTP 파일 전송**: `paramiko`를 사용하면 SFTP(Secure File Transfer Protocol)를 통해 원격 서버와 파일을 업로드하거나 다운로드할 수 있습니다.

4. **터널링 및 포트 포워딩**: `paramiko`를 사용하면 SSH 터널링과 포트 포워딩을 구현할 수 있습니다.

5. **키 관리**: `paramiko`는 SSH 공개 키와 개인 키를 생성, 저장, 로드하는 기능을 제공합니다.

`paramiko`는 주로 시스템 관리, 자동화 스크립트, 보안 통신 등의 용도로 사용됩니다. 간단한 예제 코드는 다음과 같습니다:

```python
import paramiko

# SSH 연결 및 인증
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="example.com", username="myuser", password="mypassword")

# 원격 명령 실행
stdin, stdout, stderr = client.exec_command("ls -l")
print(stdout.read().decode())

# SFTP 파일 업로드
sftp = client.open_sftp()
sftp.put("local_file.txt", "remote_file.txt")

# SSH 연결 종료
client.close()
```

이와 같이 `paramiko`는 Python에서 SSH 프로토콜을 다루는 강력한 라이브러리입니다.







paramiko.SSHClient