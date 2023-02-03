from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials

from application.utils import get_current_user
from src.patients.domain.entity import Patients
from src.patients.domain.patients_use_case import PatientsUseCase

router: APIRouter = APIRouter(prefix="/patients")


@router.get("", response_model=List[Patients])
def get_all_patients(token: HTTPAuthorizationCredentials = Depends(get_current_user)):
    """Endpoint to return all patients"""

    return PatientsUseCase().get_all()
