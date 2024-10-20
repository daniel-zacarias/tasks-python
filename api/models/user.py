from typing import Optional
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: Optional[int] = Field(None, description="Id do usuário")
    name: str = Field(..., description="Nome do usuário")
    email: str = Field(..., description="Email do usuário")
    password: str = Field(..., description="Senha do usuário")