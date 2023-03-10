from sqlalchemy import Column, String, DATETIME

from infra.db import Base


class Patients(Base):
    """Patients Model"""

    __tablename__ = "PATIENTS"

    uuid = Column(String(256), primary_key=True, name="UUID", unique=True, index=True)
    first_name = Column(String(30), name="FIRST_NAME")
    last_name = Column(String(30), name="LAST_NAME")
    date_of_birth = Column(DATETIME, name="DATE_OF_BIRTH")

    def __repr__(self):
        return f"Patient: [uuid={self.uuid}, username={self.first_name}]"
