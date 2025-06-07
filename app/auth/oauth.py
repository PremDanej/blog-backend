from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
    SecurityScopes
)
from app.auth.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/login",
    scopes={
        "user:read": "Read information about the user.",
        "blogs:read-write": "Perform Read Write operations",
        "blogs:delete": "Perform Delete operations only",
    }
)


async def get_current_user(data: Annotated[str, Depends(oauth2_scheme)], security_scopes: SecurityScopes):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )

    token_data = verify_token(data=data, credentials_exception=credentials_exception)
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value}
            )

    return token_data
