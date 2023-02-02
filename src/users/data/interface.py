from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    """Interface to Patients Repository"""

    @abstractmethod
    def get_by_uuid(self, uuid: str):
        """abstractmethod"""

        raise Exception("Method not implemented")
