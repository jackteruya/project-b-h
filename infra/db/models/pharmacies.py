from sqlalchemy import Column, String

from infra.db import Base


class Pharmacies(Base):
    """Pharmacies Model"""

    __tablename__ = "PHARMACIES"

    uuid = Column(String(256), primary_key=True, name="UUID", unique=True, index=True)
    name = Column(String(50), name="NAME")
    city = Column(String(50), name="CITY")

    def __repr__(self):
        return f"Pharmacy: [uuid={self.uuid}, name={self.name}]"
