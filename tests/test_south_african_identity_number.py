import pytest  # noqa
from za_id_number.za_id_number import SouthAfricanIdentityNumber
from za_id_number.constants import Gender, CitizenshipClass
import datetime


@pytest.fixture
def test_identity_female():
    return SouthAfricanIdentityNumber("9902200037082")


@pytest.fixture
def test_identity_male():
    return SouthAfricanIdentityNumber("2001015800085")


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


def test_gender(test_identity, test_identity_female, test_identity_male):
    # Test Female
    assert test_identity_female.gender == Gender.FEMALE.value
    # Test Female
    assert test_identity.gender == Gender.FEMALE.value
    # Test Male
    assert test_identity_male.gender == Gender.MALE.value


def test_get_citizenship(test_identity):
    assert test_identity.get_citizenship() == CitizenshipClass.CITIZEN_BORN.value


def test_citizenship(test_identity):
    assert test_identity.citizenship == CitizenshipClass.CITIZEN_BORN.value


def test_nineteenth_century():
    year = "63"
    month = "02"
    date = "20"
    test_datetime = datetime.datetime(int(f"19{year}"), int(month), int(date)).date()
    identity = SouthAfricanIdentityNumber(f"{year}{month}{date}4720082")
    assert identity.birthdate == test_datetime
    assert identity.year == test_datetime.year
    assert identity.month == test_datetime.month
    assert identity.day == test_datetime.day
