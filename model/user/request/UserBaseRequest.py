from pydantic import BaseModel


class UserBaseRequest(BaseModel):
    name: str
    email: str
    password: str
