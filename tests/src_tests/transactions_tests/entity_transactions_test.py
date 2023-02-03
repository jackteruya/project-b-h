from datetime import datetime

from src.patients.domain.entity import Patients
from src.pharmacies.domain.entity import Pharmacies
from src.transactions.domain.entity import Transactions


def test_entity_patients():
    date = datetime.now()
    patient = Patients(
        uuid="string1",
        first_name="My_name",
        last_name="My_last_name",
        date_of_birth=date,
    )

    pharmacy = Pharmacies(uuid="string2", name="My name", city="My City")

    date_2 = datetime.now()
    transaction = Transactions(
        uuid="string3",
        patient=patient,
        pharmacy=pharmacy,
        amount=100.11,
        timestamp=date_2,
    )

    assert transaction.uuid == "string3"
    assert transaction.patient.uuid == "string1"
    assert transaction.patient.first_name == "My_name"
    assert transaction.patient.last_name == "My_last_name"
    assert transaction.patient.date_of_birth == date
    assert transaction.pharmacy.uuid == "string2"
    assert transaction.pharmacy.name == "My name"
    assert transaction.pharmacy.city == "My City"
    assert transaction.amount == 100.11
    assert transaction.timestamp == date_2
