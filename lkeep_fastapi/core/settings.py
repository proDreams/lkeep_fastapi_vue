import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    NAME_DB: str = os.environ.get("NAME_DB")
    USER_DB: str = os.environ.get("USER_DB")
    PASSWORD_DB: str = os.environ.get("PASSWORD_DB")
    HOST: str = os.environ.get("HOST")
    PORT: int = int(os.environ.get("PORT"))
    ECHO: bool = bool(os.environ.get("ECHO"))
    URL: str = f"postgresql+asyncpg://{USER_DB}:{PASSWORD_DB}@{HOST}:{PORT}/{NAME_DB}"


settings = Settings()
