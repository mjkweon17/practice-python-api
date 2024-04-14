from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials

# serviceAccountKey.json 파일은 Firebase 콘솔에서 프로젝트 설정 > 서비스 계정 탭에서 생성 가능
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
