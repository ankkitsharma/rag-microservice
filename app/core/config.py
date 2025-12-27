from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "RAG System"
    environment: str = "development"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
