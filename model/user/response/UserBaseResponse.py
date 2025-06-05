from pydantic import BaseModel


class UserBaseResponse(BaseModel):
    name: str
    email: str
    # password: str

    class Config:
        orm_mode = True