from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Loads application settings from environment variables, a .env file, or other sources."""

    # Application settings
    MODE: str = "dev"  # prod
    SWAGGER_DOCS: bool = True
    REDOC_DOCS: bool = True

    # Database settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "db"
    DB_POOLSIZE: int = 20
    DB_MAXOVERFLOW: int = 20

    # Logs settings
    LOG_LEVEL: str = "INFO"

    # Auth settings
    JWT_SECRET_KEY: str = "YOUR JWT SECRET KEY"

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


stg = Settings()
