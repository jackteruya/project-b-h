from pydantic.main import BaseModel


class Users(BaseModel):
    """Transactions Entity"""

    uuid: str
    username: str
    password: str

    def __repr__(self):
        return f"User: [uuid={self.uuid}]"
