from sqlalchemy.orm import create_session

from firebase_auth import auth as firebase_auth


async def get_all_users():
    """
    Firebase에 등록된 모든 사용자 정보 가져오기
    """
    try:
        # 페이지네이션 처리를 위한 변수 초기화
        page_token = None
        all_users = []

        while True:
            # 사용자 목록 가져오기
            result = firebase_auth.list_users(page_token=page_token)

            # 가져온 사용자 정보를 리스트에 추가
            all_users.extend(result.users)

            # 다음 페이지 토큰이 있으면 계속 가져오기
            page_token = result.next_page_token
            if not page_token:
                break

        return all_users
    except Exception as e:
        print(f"Error getting all users: {e}")
        return []
