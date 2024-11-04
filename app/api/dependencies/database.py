from app.infraestructure.database import Database


async def get_db():
    session_maker = Database().session_maker()
    async with session_maker() as session:
        yield session
