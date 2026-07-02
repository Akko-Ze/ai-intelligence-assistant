from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool = False

    LLM_API_KEY: str = ""
    LLM_BASE_URL: str = ""
    LLM_MODEL: str = ""

    model_config = SettingsConfigDict(
        env_file='.env',
        extra="ignore"
    )


settings = Settings()