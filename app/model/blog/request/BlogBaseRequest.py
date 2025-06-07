from pydantic import BaseModel


class BlogBaseRequest(BaseModel):
    title: str
    body: str