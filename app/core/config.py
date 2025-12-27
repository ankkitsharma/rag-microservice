from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "RAG System"
    environment: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
