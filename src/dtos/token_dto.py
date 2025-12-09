from pydantic import BaseModel


class TokenDTO(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int