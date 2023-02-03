from datetime import datetime

from pydantic.main import BaseModel


class Patient(BaseModel):
    """Patient Entity"""

    uuid: str
    first_name: str
    last_name: str
    date_of_birth: datetime

    def __repr__(self):
        return f"Patient: [uuid={self.uuid}]"
