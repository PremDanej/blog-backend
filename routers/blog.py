from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from connection.connection import get_database
from model.blog.request.BlogBaseRequest import BlogBaseRequest
from model.blog.request.BlogWithUserRequest import BlogWithUserRequest
from model.blog.response.BlogBaseResponse import BlogBaseResponse
from model.blog.response.BlogWithUserResponse import BlogWithUserResponse
from repository.blog import blog_repository
from schema.user.UserTable import User
from auth.oauth import get_current_user

router = APIRouter(
    tags=["Blog"],
    prefix="/api/v1/blog"
)


@router.get("", response_model=list[BlogBaseResponse], status_code=status.HTTP_200_OK)
def all_blogs(db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    return blog_repository.get_all(db)


@router.get("/{id}", response_model=BlogWithUserResponse, status_code=status.HTTP_200_OK)
def show_blog(id: int, db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    return blog_repository.show_blog(id, db)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_blog(request: BlogWithUserRequest, db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    return blog_repository.create_blog(request, db)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_blog(id: int, request: BlogBaseRequest, db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    return blog_repository.update_blog(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    return blog_repository.delete_blog(id, db)
