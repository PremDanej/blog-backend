from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from hasing.hasing import Hash
from model.user.request.UserBaseRequest import UserBaseRequest
from schema.user.UserTable import User


def create_user(request: UserBaseRequest, db: Session):
    hash_password = Hash.get_password_hash(request.password)
    user = User(name=request.name, email=request.email, password=hash_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def all_users(db: Session):
    users = db.query(User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong!."
        )
    return users


def show_user(id: int, db: Session):
    users = db.query(User).filter(User.id == id).first()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    return users
