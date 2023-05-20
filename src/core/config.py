from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator

BASE_DIR = Path('__file__').resolve().parent
env_path = BASE_DIR / '.env'


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI PostgreSQL"
    PROJECT_VERSION: str = "1.0"
    API_V1_STR: str = "/api/v1"

    # Database
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str],
                               values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    MEDIA_ROOT: str = str(BASE_DIR / 'media')

    class Config:
        env_file = env_path
        case_sensitive = True


settings = Settings()