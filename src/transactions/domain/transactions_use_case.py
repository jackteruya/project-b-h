from repository.transactions_repository import TransactionsRepository
from src.patients.domain.patients_use_case import PatientsUseCase
from src.pharmacies.domain.pharmacies_use_case import PharmaciesUseCase
from src.transactions.domain.entity import Transactions


class TransactionsUseCase:
    """Transactions Use Case"""

    def __init__(self, transactions_repository=TransactionsRepository):
        self._repository = transactions_repository

    def get_all(self):
        """Return all transactions"""
        transactions_list = [
            Transactions(
                uuid=transaction.uuid,
                patient=PatientsUseCase().get_by_uuid(transaction.patient_uuid),
                pharmacy=PharmaciesUseCase().get_by_uuid(transaction.pharmacy_uuid),
                amount=transaction.amount,
                timestamp=transaction.timestamp,
            )
            for transaction in self._repository().get_all()
        ]
        return transactions_list
