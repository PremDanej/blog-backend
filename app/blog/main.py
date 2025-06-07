from fastapi import FastAPI
from app.connection.connection import engine
from app.routers import (
    blog,
    login
)
from app.routers import user
from app.schema.Base import Base

Base.metadata.create_all(engine)
app = FastAPI()


@app.get("/")
def home():
    return "Welcome to Blog"


app.include_router(router=login.router)
app.include_router(router=blog.router)
app.include_router(router=user.router)
