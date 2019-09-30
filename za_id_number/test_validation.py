import pytest
from za_identity_number import SouthAfricanIdentityValidate

def test_validation():
    validate = SouthAfricanIdentityValidate("9202204720082")

    assert validate.validate()

def test_identity():
    identity = SouthAfricanIdentityValidate("9202204720082").identity()

    assert identity["year"] == "92"
    assert identity["month"] == "02"
    assert identity["day"] == "20"
    assert identity["gender"] == "Female"
