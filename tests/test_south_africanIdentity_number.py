import pytest  # noqa
from za_id_number.za_id_number import SouthAfricanIdentityNumber
from datetime import datetime


@pytest.fixture
def test_identity():
    return SouthAfricanIdentityNumber("9001245289086")

def test_year(test_identity):
    assert test_identity.year == 1990


def test_get_year(test_identity):
    assert test_identity.get_year() == 1990

def test_is_datetime(test_identity):
    assert test_identity.is_datetime(test_identity.birthdate)