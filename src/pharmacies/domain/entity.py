from pydantic.main import BaseModel


class Pharmacies(BaseModel):
    """Pharmacy Entity"""

    uuid: str
    name: str
    city: str

    def __repr__(self):
        return f"Pharmacy: [uuid={self.uuid}]"
