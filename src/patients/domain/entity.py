from datetime import datetime

from pydantic import BaseModel


class Patient(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    date_of_birth: datetime
