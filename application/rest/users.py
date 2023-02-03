from datetime import timedelta
from os import getenv

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from starlette import status

from application.schema.users_schema import UserSchema
from application.utils import Password, create_access_token
from src.users.domain.users_use_case import UsersUseCase

load_dotenv()

router: APIRouter = APIRouter(prefix="/users")


@router.post("")
def register_user(user: UserSchema):
    """Register user"""

    try:
        password = Password().get_password_hash(user.password)
        return UsersUseCase().create_user(user.username, password)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="username já cadastrado",
        )


@router.post("/token")
def login_for_access_token(user_data: UserSchema):
    """Generate token"""

    user = UsersUseCase().get_user_by_username(user_data.username)
    if not Password().verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
