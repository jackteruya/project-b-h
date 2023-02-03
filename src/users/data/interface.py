from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    """Interface to Patients Repository"""

    @abstractmethod
    def get_by_username(self, username: str):
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def create_user(self, username: str, password: str):
        """abstractmethod"""

        raise Exception("Method not implemented")
