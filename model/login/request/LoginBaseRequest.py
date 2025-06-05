from pydantic import BaseModel


class LoginBaseRequest(BaseModel):
    username: str
    password: str
