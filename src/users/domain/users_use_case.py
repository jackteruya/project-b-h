from repository.users_repository import UsersRepository
from src.users.domain.entity import Users


class UsersUseCase:
    """Users Use Case"""

    def __init__(self, users_repository=UsersRepository):
        self._repository = users_repository

    def create_user(self, username: str, password: str):
        """Create User"""
        user = self._repository().get_by_username(username)
        if user:
            raise ValueError("Usuario já cadastrado")
        user = self._repository().create_user(username, password)
        return {"user_uuid": user.uuid}

    def get_user_by_username(self, username: str):
        """Get user by username"""
        user = self._repository().get_by_username(username)
        user = Users(**user.__dict__)
        return user
