from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.api.dependencies.security import hash_password
from app.schemas.user import UserModel
from app.domain.services.user import create_user as service
from app.api.dependencies.database import get_db
from app.schemas.user import InputCreateUserDto
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(user: InputCreateUserDto,
                      session: AsyncSession = Depends(get_db)):
    user_model = UserModel(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    try:
        async with session:
            output = await service(user_model, session)
            return JSONResponse(
                status_code=201,
                content=output.model_dump()
            )
    except IntegrityError:
        return JSONResponse(
            status_code=400,
            content={
                "Message": "Email alredy exists"
            }
        )
