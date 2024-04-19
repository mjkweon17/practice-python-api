import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

load_dotenv(dotenv_path)


class Settings(BaseSettings):
    # SSH 설정
    SSH_HOST: str = os.getenv("SSH_HOST", "localhost")
    SSH_PORT: int = int(os.getenv("SSH_PORT", 22))
    SSH_USERNAME: str = os.getenv("SSH_USERNAME", "username")
    SSH_PASSWORD: str = os.getenv("SSH_PASSWORD", "password")
    SSH_PEM_KEY: str = os.getenv("SSH_PEM_KEY", "path/to/pem/key")

    # 데이터베이스 설정
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 3306))
    DB_NAME: str = os.getenv("DB_NAME", "library_db")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")

    # Container Registry 설정
    CONTAINER_USERNAME: str = os.getenv("CONTAINER_USERNAME", "username")
    CONTAINER_PASSWORD: str = os.getenv("CONTAINER_PASSWORD", "password")
    CONTAINER_REGISTRY: str = os.getenv("CONTAINER_REGISTRY", "docker.io")
    CONTAINER_IMAGE: str = os.getenv("CONTAINER_IMAGE", "kubbok")
    CONTAINER_TAG: str = os.getenv("CONTAINER_TAG", "latest")

    # OpenAI API 설정
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "your-openai-api-key")

    # JWT 토큰 설정
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_EXPIRATION_TIME_MINUTES: int = int(os.getenv("JWT_ACCESS_EXPIRATION_TIME_MINUTES", 30))
    JWT_REFRESH_EXPIRATION_TIME_MINUTES: int = int(os.getenv("JWT_REFRESH_EXPIRATION_TIME_MINUTES", 60))

    # 애플리케이션 설정
    APP_TITLE: str = "Library Management System"
    APP_DESCRIPTION: str = "API for managing library resources"
    APP_VERSION: str = "0.1.0"

    # Firebase 설정
    FIREBASE_SERVICE_ACCOUNT_KEY: str = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY", "firebase-service-account-key.json")
    FIREBASE_WEB_API_KEY: str = os.getenv("FIREBASE_WEB_API_KEY", "firebase-web-api-key")
