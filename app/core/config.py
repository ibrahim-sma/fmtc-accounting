from pydantic_settings import BaseSettings

secret_key: str = "CHANGE_THIS_SECRET"
algorithm: str = "HS256"
access_token_expire_minutes: int = 60


class Settings(BaseSettings):
    app_name: str = "Accounting App"
    debug: bool = True

    class Config:
        env_prefix = ""   # allows APP_NAME → app_name

settings = Settings()
