import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class DBSettings(BaseSettings):
    NAME: str = os.environ.get("DB_NAME")
    USER: str = os.environ.get("DB_USER")
    PASSWORD: str = os.environ.get("DB_PASSWORD")
    HOST: str = os.environ.get("DB_HOST")
    PORT: int = int(os.environ.get("DB_PORT"))
    ECHO: bool = bool(os.environ.get("DB_ECHO"))
    URL: str = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"


class Settings(BaseSettings):
    db_settings: DBSettings = DBSettings()
    REDIS_HOST: str = os.environ.get("REDIS_HOST")
    REDIS_PORT: int = int(os.environ.get("REDIS_PORT"))
    SECRET_KEY: str = os.environ.get("SECRET_KEY")


settings = Settings()
