- https://firebase.google.com/docs/auth?hl=ko

- 주요 기능: FirebaseUI 인증 / Firebase SDK 인증
    - FirebaseUI 인증은 전체 로그인 시스템을 추가할 때 사용하는 방법으로 프론트에서 주로 사용하는 것 같음
    - 나는 백엔드 서버에서 Firebase의 인증 기능만 이용할 것이므르 Firebase SDK를 사용하겠음
- Firebase SDK 인증
    - 방법: 이메일 및 비밀번호 기반 인증 / ID 공급업체 통합
    - 현재 LMS에 이메일과 비밀번호로 auth를 관리하고 있기 때문에 쿠책책에서도 이메일과 비밀번호로 auth를 관리하겠음
    - 그런데 위 링크에는 iOS, 안드로이드, 웹, C++, Unity는 있는데 파이선은 보이지 않음
- 기본 원리
    - 사용자를 앱에 로그인시키기 위해 사용자에게서 인증 정보를 받아야 함. 우리가 받아 올 인증 정보는 이메일 주소와 비밀번호. 인증 벙보를 Firebase 인증 SDK로 전달하면 Firebase의 백엔드 서비스가 정보를 확인하고 클라이언트에 응답을 반환함.


    OAuth 리디렉션 URL
    ID 공급업체