from fastapi import FastAPI
from connection.connection import engine
from routers import (
    user,
    blog,
    login
)
from schema.Base import Base

Base.metadata.create_all(engine)
app = FastAPI()


@app.get("/")
def home():
    return "Welcome to Blog"


app.include_router(router=login.router)
app.include_router(router=blog.router)
app.include_router(router=user.router)
