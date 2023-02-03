from pydantic import BaseModel


class TokenData(BaseModel):
    """Token data"""

    username: str | None = None

    def __repr__(self):
        return f"TokenData: [username={self.username}]"


class UserSchema(BaseModel):
    """User Schema"""

    username: str
    password: str

    def __repr__(self):
        return f"UserSchema: [username={self.username}]"
