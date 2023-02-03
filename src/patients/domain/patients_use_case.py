from repository.patients_repository import PatientsRepository
from src.patients.domain.entity import Patients


class PatientsUseCase:
    """Patients Use Case"""

    def __init__(self, patients_repository=PatientsRepository):
        self._repository = patients_repository

    def get_all(self):
        """Return all patients"""
        patients_list = [
            Patients(**patient.__dict__) for patient in self._repository().get_all()
        ]
        return patients_list

    def get_by_uuid(self, uuid: str):
        """Return patient by uuid"""
        return Patients(**self._repository().get_by_uuid(uuid).__dict__)
