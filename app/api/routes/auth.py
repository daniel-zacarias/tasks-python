from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies.database import get_db
from app.schemas.token import TokenOutputDto
from app.schemas.user import OutputTokenUserDto
from app.api.dependencies.security import authenticate_user, create_access_token, get_current_user
from app.constants import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter()


@router.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session=Depends(get_db)
) -> TokenOutputDto:
    user = await authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return TokenOutputDto(access_token=access_token, token_type="bearer")


@router.get("/users/me/")
async def read_users_me(
    current_user: OutputTokenUserDto = Depends(get_current_user),
):
    return current_user
