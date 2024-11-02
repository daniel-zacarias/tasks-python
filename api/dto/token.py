from pydantic import BaseModel


class TokenOutputDto(BaseModel):
    access_token: str
    token_type: str
