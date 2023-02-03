from datetime import datetime, timedelta
from os import getenv

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette import status

from application.schema.users_schema import TokenData
from src.users.domain.users_use_case import UsersUseCase

load_dotenv()


class Password:
    """Password tools"""

    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        """Validate password"""

        return self._pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        """Create hash"""
        return self._pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create Token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM")
    )
    return encoded_jwt


def get_current_user(token: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    """Validate toke user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not token:
        raise credentials_exception
    try:
        payload = jwt.decode(
            token.credentials, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = UsersUseCase().get_user_by_username(token_data.username)
    if user is None:
        raise credentials_exception
    return user
