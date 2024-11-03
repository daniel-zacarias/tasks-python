from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError, decode, encode
from api.connectors.db_connection_session import Database
from api.services.user import get_user
from api.utils.cripto_password import verify_password
from constants import SECRET_KEY
from api.dto.user import OutputTokenUserDto

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def authenticate_user(username: str, password: str, session):
    user = await get_user(username, session)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme),
                           session=Depends(Database().session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = {
            "email": username
        }
    except InvalidTokenError:
        raise credentials_exception
    user = await get_user(token_data["email"], session)
    if user is None:
        raise credentials_exception
    return OutputTokenUserDto(
        id=user.id,
        name=user.name,
        email=user.email
    )
