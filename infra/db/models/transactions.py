from sqlalchemy import Column, String, NUMERIC, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

from infra.db import Base


class Transactions(Base):
    __tablename__ = "TRANSACTIONS"

    uuid = Column(String(256), primary_key=True, name="UUID", unique=True, index=True)
    patient_uuid = Column(String(256), ForeignKey("PATIENTS.UUID"), name="PATIENT_UUID")
    patient = relationship("Patients")
    pharmacy_uuid = Column(
        String(256), ForeignKey("PHARMACIES.UUID"), name="PHARMACY_UUID"
    )
    pharmacy = relationship("Pharmacies")
    amount = Column(NUMERIC, name="AMOUNT")
    timestamp = Column(DATETIME(timezone=True), name="TIMESTAMP", autoincrement=True)
