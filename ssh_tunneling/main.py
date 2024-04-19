import paramiko
from io import StringIO
import os
import pymysql

from config import Settings

settings = Settings()

# private key를 paramiko.RSAKey 객체로 변환
private_key = paramiko.RSAKey.from_private_key(StringIO(os.getenv('SSH_PEM_KEY')))

# SSH 연결 및 인증
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(
    settings.SSH_HOST,
    port=settings.SSH_PORT,
    username=settings.SSH_USERNAME,
    password=settings.SSH_PASSWORD,
    pkey=private_key,
)

# SSH 터널링 설정
ssh_transport = ssh_client.get_transport()
local_port = 3306  # 로컬의 포트 번호
remote_host = settings.DB_HOST
remote_port = 3306  # 원격 데이터베이스의 포트 번호
ssh_transport.request_port_forward(remote_host, remote_port)
local_forward_channel = ssh_transport.open_channel("direct-tcpip", (remote_host, remote_port), ("127.0.0.1", local_port))

# 데이터베이스 연결
db_connection = pymysql.connect(
    host=settings.DB_HOST,
    port=local_port,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    database=settings.DB_NAME,
)

# 사용 후 연결 닫기
db_connection.close()



# SSH 연결 닫기
ssh_client.close()