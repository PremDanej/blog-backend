from pydantic import BaseModel


class BlogWithUserRequest(BaseModel):
    user_id: int
    title: str
    body: str
