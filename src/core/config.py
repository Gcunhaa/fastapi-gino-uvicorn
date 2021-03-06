from pydantic import BaseSettings
from sqlalchemy.engine.url import URL

class Settings(BaseSettings):
    API_VERSION_STR : str = "/v1"
    PROJECT_NAME : str = "Fastapi-gino-uvicorn"
    VERSION: str = "0.0.0"

    POSTGRES_SERVER: str = "lallah.db.elephantsql.com"
    POSTGRES_USER: str = "qifealev"
    POSTGRES_PASSWORD: str = "tnmtOSFsY0yf46nLNcoF_Q3QKVRTkVuF"
    POSTGRES_DB: str = "qifealev"
    POSTGRES_PORT: int = 5432

    class Config:
        case_sensitive = True
    
    def get_postgres_dsn(self):
        return f"asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

    def get_alembic_dsn(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

settings = Settings()