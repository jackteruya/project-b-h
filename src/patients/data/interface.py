from abc import ABC, abstractmethod


class PatientsRepositoryInterface(ABC):
    """Interface to Patients Repository"""

    @abstractmethod
    def get_all(self):
        raise Exception("Method not implemented")