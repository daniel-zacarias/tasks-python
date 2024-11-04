from typing import Optional
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: Optional[int] = Field(None, description="Id do usuário")
    name: str = Field(..., description="Nome do usuário")
    email: str = Field(..., description="Email do usuário")
    password: str = Field(..., description="Senha do usuário")


class InputCreateUserDto(BaseModel):
    name: str = Field(..., description="Nome do usuário")
    email: str = Field(..., description="Email do usuário")
    password: str = Field(..., description="Senha do usuário")


class OutputCreateUserDto(BaseModel):
    id: int = Field(..., description="Id do usuário")
    name: str = Field(..., description="Nome do usuário")
    email: str = Field(..., description="Email do usuário")


class OutputTokenUserDto(BaseModel):
    id: int = Field(..., description="Id do usuário")
    name: str = Field(..., description="Nome do usuário")
    email: str = Field(..., description="Email do usuário")