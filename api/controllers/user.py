from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from api.models.user import UserModel
from api.services.user import create_user as service
from api.connectors.db_connection_session import Database
from api.dto.user import InputCreateUserDto
from api.utils.cripto_password import hash_password
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(user: InputCreateUserDto,
                      session: AsyncSession = Depends(Database().session)):
    user_model = UserModel(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    try:
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
