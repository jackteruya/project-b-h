import uuid
from sqlalchemy import Column, String

from infra.db import Base


class Users(Base):
    """Users Model"""

    __tablename__ = "USERS"

    uuid = Column(
        String(256),
        primary_key=True,
        name="UUID",
        unique=True,
        index=True,
        default=str(uuid.uuid4()),
    )
    username = Column(String(50), name="USERNAME")
    password = Column(String(256), name="PASSWORD")

    def __repr__(self):
        return f"User: [uuid={self.uuid}, username={self.username}]"
