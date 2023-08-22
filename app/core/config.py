import logging
from typing import Optional

from pydantic import BaseSettings, EmailStr

from app.core.constants import LOG_DT_FORMAT, LOG_FORMAT


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    description: str = 'Помогаем котикам вместе'
    database_url: str = 'sqlite+aiosqlite:///./cat_charity.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
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


def configure_logging():
    logging.basicConfig(
        datefmt=LOG_DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(logging.StreamHandler(),)
    )


settings = Settings()
