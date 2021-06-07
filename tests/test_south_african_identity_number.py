import pytest  # noqa
from za_id_number.za_id_number import SouthAfricanIdentityNumber
from za_id_number.constants import Gender, Citizen
from datetime import datetime


@pytest.fixture
def test_identity():
    return SouthAfricanIdentityNumber("9902204720082")

def test_year(test_identity):
    assert test_identity.year == 1999

def test_get_year(test_identity):
    assert test_identity.get_year() == 1999

def test_month(test_identity):
    assert test_identity.month == 2

def test_get_month(test_identity):
    assert test_identity.get_month() == 2

def test_day(test_identity):
    assert test_identity.day == 20

def test_get_day(test_identity):
    assert test_identity.get_day() == 20

def test_gender(test_identity):
    assert test_identity.gender == Gender.MALE.value