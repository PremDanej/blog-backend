from pydantic import BaseModel


class LoginBaseResponse(BaseModel):
    access_token: str
    token_type: str
