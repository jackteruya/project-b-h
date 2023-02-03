from repository.pharmacies_repository import PharmaciesRepository
from src.pharmacies.domain.entity import Pharmacies


class PharmaciesUseCase:
    """Pharmacy Use Case"""

    def __init__(self, pharmacies_repository=PharmaciesRepository):
        self._repository = pharmacies_repository

    def get_all(self):
        """Return all pharmacies"""
        pharmacies_list = [
            Pharmacies(**pharmacy.__dict__) for pharmacy in self._repository().get_all()
        ]
        return pharmacies_list

    def get_by_uuid(self, uuid: str):
        """Return pharmacy by uuid"""
        return Pharmacies(**self._repository().get_by_uuid(uuid).__dict__)
