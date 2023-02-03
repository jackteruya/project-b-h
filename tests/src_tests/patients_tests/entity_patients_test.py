from datetime import datetime

from src.patients.domain.entity import Patients


def test_entity_patients():
    date = datetime.now()
    patient = Patients(
        uuid="string",
        first_name="My_name",
        last_name="My_last_name",
        date_of_birth=date,
    )

    assert patient.uuid == "string"
    assert patient.first_name == "My_name"
    assert patient.last_name == "My_last_name"
    assert patient.date_of_birth == date
