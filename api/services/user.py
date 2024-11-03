from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.dto.user import OutputCreateUserDto
from api.entities.user import User
from api.models.user import UserModel


async def create_user(user: UserModel, session: AsyncSession):
    insert_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    session.add(insert_user)
    await session.commit()
    await session.refresh(insert_user)
    return OutputCreateUserDto(
        id=insert_user.id,
        name=insert_user.name,
        email=insert_user.email
    )


async def get_user(email: str, session: AsyncSession):
    result = await session.execute(select(User).where(User.email == email))
    user = result.scalar_one()
    return user
