from abc import ABC, abstractmethod


class TransactionsRepositoryInterface(ABC):
    """Interface to Patients Repository"""

    @abstractmethod
    def get_all(self):
        """abstractmethod"""

        raise Exception("Method not implemented")
