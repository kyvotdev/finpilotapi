from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from core.config import stg


engine = create_async_engine(
    url=stg.DB_URL,
    pool_size=stg.DB_POOLSIZE,
    max_overflow=stg.DB_MAXOVERFLOW,
)
session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as ses:
        yield ses
