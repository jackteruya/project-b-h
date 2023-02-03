from src.pharmacies.domain.entity import Pharmacies


def test_entity_pharmacies():
    pharmacy = Pharmacies(uuid="string", name="My name", city="My City")

    assert pharmacy.uuid == "string"
    assert pharmacy.name == "My name"
    assert pharmacy.city == "My City"
