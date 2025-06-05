from pydantic import BaseModel
from typing import List
from model.user.response.UserBaseResponse import UserBaseResponse


class BlogWithUserResponse(BaseModel):
    title: str
    body: str
    creator: UserBaseResponse

    class Config:
        orm_mode = True