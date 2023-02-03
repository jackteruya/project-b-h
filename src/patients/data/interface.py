from abc import ABC, abstractmethod


class PatientsRepositoryInterface(ABC):
    """Interface to Patients Repository"""

    @abstractmethod
    def get_all(self):
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def get_by_uuid(self, uuid: str):
        """abstractmethod"""

        raise Exception("Method not implemented")
