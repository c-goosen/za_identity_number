import pytest
from .za_identity_number import SouthAfricanIdentityValidate

def test_validation():
    validate = SouthAfricanIdentityValidate("9202204720082")
    assert validate.validate()

def test_identity():
    identity = SouthAfricanIdentityValidate("9202204720082").identity()
    assert identity["year"] == "92"
    assert identity["month"] == "02"
    assert identity["day"] == "20"
    assert identity["gender"] == "Male"
    assert not identity["valid"] #not actual ID number, example on website

def test_identity_types():
    identity = SouthAfricanIdentityValidate("9202204720082").identity()

    assert isinstance(identity, dict)
    assert isinstance(identity["gender"], str)
    assert isinstance(identity["year"], str)


def test_validation_negative():
    validate = SouthAfricanIdentityValidate("9902204720089")
    assert not validate.validate()

def test_identity_negative():
    identity = SouthAfricanIdentityValidate("9902204720082").identity()
    assert identity["year"] != "92"
    assert identity["month"] != "03"
    assert identity["day"] != "33"
    assert identity["gender"] != "Female"
    assert not identity["valid"] 


