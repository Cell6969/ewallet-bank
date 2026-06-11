from app.config import db_settings
from  sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url=db_settings.get_db_connection,
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600
)

async_session = async_sessionmaker(
    bind=engine,
    class_= AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()


# Initiate Base Classes
class BaseModel(DeclarativeBase):
    pass