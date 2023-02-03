from typing import List

from fastapi import APIRouter

from src.pharmacies.domain.entity import Pharmacies
from src.pharmacies.domain.pharmacies_use_case import PharmaciesUseCase

router: APIRouter = APIRouter(prefix="/pharmacies")


@router.get("", response_model=List[Pharmacies])
def get_all_pharmacies():
    """Endpoint to return all pharmacies"""

    return PharmaciesUseCase().get_all()
