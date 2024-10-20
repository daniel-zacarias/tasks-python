from contextlib import contextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from api.entities.base import CommonFields
from constants import DATABASE_URL


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.engine = create_async_engine(DATABASE_URL, echo=True)
            cls._instance.async_session = async_sessionmaker(bind=cls._instance.engine, expire_on_commit=False)
        return cls._instance

    async def session(self):
        async with self.async_session() as session:
            yield session

    async def init_models(self):
        self.engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})
        async with self.engine.begin() as conn:
            await conn.run_sync(CommonFields.metadata.drop_all)
            await conn.run_sync(CommonFields.metadata.create_all)