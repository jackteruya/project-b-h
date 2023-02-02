from abc import ABC, abstractmethod


class PharmaciesRepositoryInterface(ABC):
    """Interface to Patients Repository"""

    @abstractmethod
    def get_all(self):
        raise Exception("Method not implemented")
