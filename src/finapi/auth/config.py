from datetime import timedelta

from authx import AuthX, AuthXConfig

from finapi.core.config import stg


config = AuthXConfig(
    JWT_SECRET_KEY=stg.JWT_SECRET_KEY,
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=15),
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=5),
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)
