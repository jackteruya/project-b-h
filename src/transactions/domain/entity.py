from datetime import datetime

from pydantic.main import BaseModel

from src.patients.domain.entity import Patients
from src.pharmacies.domain.entity import Pharmacies


class Transactions(BaseModel):
    """Transactions Entity"""

    uuid: str
    patient: Patients
    pharmacy: Pharmacies
    amount: float
    timestamp: datetime

    def __repr__(self):
        return f"Transactions: [uuid={self.uuid}]"
