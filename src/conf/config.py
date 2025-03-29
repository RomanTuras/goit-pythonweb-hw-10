from pydantic import ConfigDict, EmailStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # MAIL_USERNAME: EmailStr = "salden.com@meta.ua"
    MAIL_USERNAME: EmailStr = "admin@skinia.pl"
    # MAIL_PASSWORD: str = "ttY-rZ@5e7"
    MAIL_PASSWORD: str = "s412bc123"
    MAIL_FROM: EmailStr = "admin@skinia.pl"
    # MAIL_FROM: EmailStr = "salden.com@meta.ua"
    MAIL_SERVER: str = "h87.hvosting.ua"
    # MAIL_SERVER: str = "smtp.meta.ua"
    MAIL_PORT: int = 465
    MAIL_FROM_NAME: str = "Rest API Service"
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = True
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    model_config = ConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

settings = Settings()


class Config:
    DB_URL = "postgresql+asyncpg://postgres:fE512@localhost:5432/contacts"
    JWT_SECRET = "44_02_76"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_SECONDS = 3600

config = Config
