from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHMEY_DATABASE_URL = settings.DATABASE_URL
engine = create_async_engine(SQLALCHMEY_DATABASE_URL, future=True, echo=True)
async_engine = sessionmaker(
    engine, autocommit=False, autoflush=False, class_=AsyncSession
)
