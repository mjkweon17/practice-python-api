# 1. Firebase Admin SDK 설치
# pip install firebase-admin

# 2. Firebase프로젝트에 서비스 계정 키 파일 다운로드
#     Firebase 콘솔에서 프로젝트 설정으로 이동합니다.
#     "서비스 계정" 탭에서 "새 비공개 키 생성"을 클릭하여 키 파일을 다운로드합니다.

##### 3. FastAPI 프로젝트에 Firebase 초기화: #####
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# 4. FastAPI에 인증 미들웨어 생성
app = FastAPI()


@app.middleware("http")
async def firebase_auth_middleware(request: Request, call_next):
    try:
        token = request.headers.get("Authorization")
        if token:
            decoded_token = auth.verify_id_token(token.split(" ")[1])
            request.state.user = decoded_token
        else:
            request.state.user = None
    except Exception as e:
        return JSONResponse(status_code=401, content={"error": str(e)})

    response = await call_next(request)
    return response

##### 5. 보호된 경로 생성 #####


def get_current_user(request: Request):
    user = request.state.user
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    return user


@app.get("/protected")
async def protected_route(current_user=Depends(get_current_user)):
    return {"message": "Authentication successful"}
