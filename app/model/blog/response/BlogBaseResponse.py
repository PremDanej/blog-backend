from pydantic import BaseModel


class BlogBaseResponse(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True