from typing import List

from fastapi import APIRouter

from src.patients.domain.entity import Patient
from src.patients.domain.patients_use_case import PatientsUseCase

router: APIRouter = APIRouter(prefix="/patients")


@router.get("", response_model=List[Patient])
def get_patients_by_uuid():
    """Endpoint to return all patients"""

    return PatientsUseCase().get_all()
