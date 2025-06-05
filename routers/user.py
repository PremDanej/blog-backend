from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from connection.connection import get_database
from model.user.request.UserBaseRequest import UserBaseRequest
from model.user.response.UserBaseResponse import UserBaseResponse
from model.user.response.UserWithBlogsResponse import UserWithBlogResponse
from repository.user import user_repository

router = APIRouter(
    tags=["User"],
    prefix="/api/v1/user"
)


@router.post("", response_model=UserBaseResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: UserBaseRequest, db: Session = Depends(get_database)):
    return user_repository.create_user(request, db)


@router.get("", response_model=list[UserBaseResponse], status_code=status.HTTP_200_OK)
def all_users(db: Session = Depends(get_database)):
    return user_repository.all_users(db)


@router.get("/{id}", response_model=UserWithBlogResponse, status_code=status.HTTP_200_OK)
def show_user(id: int, db: Session = Depends(get_database)):
    return user_repository.show_user(id, db)
