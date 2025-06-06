from datetime import timedelta
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from hasing.hasing import Hash
from connection.connection import get_database
from model.login.response.LoginBaseResponse import LoginBaseResponse
from schema.user.UserTable import User
from auth import token

router = APIRouter(
    tags=["Authentication"],
    prefix="/api/v1"
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_database)):
    # here [request.username] act as email
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "bearer"},
        )

    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email, "scopes": request.scopes},
        expires_delta=access_token_expires
    )
    return LoginBaseResponse(access_token=access_token, token_type="bearer")
