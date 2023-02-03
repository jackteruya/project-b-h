from repository.patients_repository import PatientsRepository
from src.patients.domain.entity import Patient


class PatientsUseCase:
    def __init__(self, patients_repository=PatientsRepository):
        self._repository = patients_repository

    def get_all(self):
        patients_list = [
            Patient(**patient.__dict__) for patient in self._repository().get_all()
        ]
        return patients_list
