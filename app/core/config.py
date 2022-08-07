from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд (0.1.0)'
    description: str = 'Сервис для поддержки котиков!'
    database_url: str = 'sqlite+aiosqlite:///./qrkot.db'
    authentication_backend: str = 'jwt'
    secret: str = 'SECRET'
    min_password_length: int = 3
    # google api
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = '.env'


class Sheets:
    UPDATE_RANGE: str = 'A1:E30'
    TITLE: str = 'Лист1'
    VERSION: str = 'v4'
    LOCALE: str = 'ru_RU'
    TYPE: str = 'GRID'
    ID: int = 0
    ROW_COUNT: int = 100
    COLUMN_COUNT: int = 11
    DT_FORMAT: str = "%Y/%m/%d %H:%M:%S"


class Drive:
    VERSION: str = 'v3'


settings = Settings()
