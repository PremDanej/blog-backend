from pydantic import BaseModel
from typing import List

from app.model.blog.response.BlogBaseResponse import BlogBaseResponse


class UserWithBlogResponse(BaseModel):
    name: str
    email: str
    blogs: List[BlogBaseResponse]