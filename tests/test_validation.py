import pytest  # noqa
from za_id_number.za_id_number import SouthAfricanIdentityValidate
import datetime
from za_id_number.constants import LIB_DATE_FORMAT

from dateutil.relativedelta import relativedelta
from dataclasses import dataclass


@dataclass
class DateTimeTest:
    """Class for keeping track of an item in inventory."""

    year: str = "90"
    month: str = "01"
    date: str = "24"


"""
Fixtures
"""


@pytest.fixture
def test_identity_birthdate():
    birthday = DateTimeTest()
    return (
        SouthAfricanIdentityValidate(
            f"{birthday.year}{birthday.month}{birthday.date}5289086"
        ),
        birthday,
    )


@pytest.fixture
def test_true_identity():
    return SouthAfricanIdentityValidate("9001245289086")


@pytest.fixture
def test_false_identity():
    return SouthAfricanIdentityValidate("9902204720082")


"""
Tests
"""


def test_validation(test_true_identity):
    assert test_true_identity.validate()


def test_identity(test_true_identity):
    identity_obj = test_true_identity.identity()
    assert identity_obj["year"] == 1990
    assert identity_obj["month"] == 1
    assert identity_obj["day"] == 24
    assert identity_obj["gender"] == "Male"
    assert identity_obj["valid"]


def test_identity_types(test_true_identity):
    identity = test_true_identity.identity()
    assert isinstance(identity, dict)
    assert isinstance(identity["gender"], str)
    assert isinstance(identity["year"], int)
    assert isinstance(identity["month"], int)
    assert isinstance(identity["day"], int)
    assert isinstance(identity["birthdate"], datetime.date)
    assert isinstance(identity["age"], int)


def test_validation_negative(test_false_identity):
    assert not test_false_identity.validate()


def test_birthdate_elements(test_true_identity):
    identity_obj = test_true_identity.identity()
    assert identity_obj["year"] != 1992
    assert identity_obj["month"] != 3
    assert identity_obj["day"] != 33


def test_identity_negative(test_false_identity):
    identity_obj = test_false_identity.identity()
    print(identity_obj)
    assert not identity_obj["valid"]


def test_age():
    year = "99"
    start_date = datetime.datetime.strptime(f"{year}-02-20", LIB_DATE_FORMAT)
    end_date = datetime.date.today()
    age = int(relativedelta(end_date, start_date).years)
    assert SouthAfricanIdentityValidate(f"{year}02204720082").get_age() == age


def test_birthdate(test_identity_birthdate):
    birthdate = test_identity_birthdate[0].birthdate
    year = test_identity_birthdate[1].year
    month = test_identity_birthdate[1].month
    date = test_identity_birthdate[1].date
    assert (
        birthdate
        == datetime.datetime.strptime(f"{year}-{month}-{date}", LIB_DATE_FORMAT).date()
    )


def test_all_zeroes():
    """
    This is a strange case.
    On the one hand with luhn algorithm would test correct.
    But as ZA Id number you couldn't have the age of 00 00 00
    """
    valid = SouthAfricanIdentityValidate("0000000000000").validate()
    assert not valid


def test_alphabetical():
    valid = SouthAfricanIdentityValidate("123456ABC7890").validate()
    assert not valid


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("0000000000000", False),
        ("0000000000001", False),
        ("0010000000000", False),
        ("00100000000001", False),
    ],
)
def test_edge_cases_validate(test_input, expected):
    assert expected == SouthAfricanIdentityValidate(test_input).validate()


def test_github_issue_4():
    valid = SouthAfricanIdentityValidate("0000000000000").validate()
    assert not valid


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("9902204720082", True),
        ("990220472008", False),
        ("99022047200", False),
        ("9902204720", False),
        ("990220472", False),
        ("99022047", False),
        ("9902204", False),
        ("990220", False),
        ("99022", False),
        ("9902", False),
        ("990", False),
        ("99", False),
        ("9", False),
        ("99022047200821", False),
        ("990220472008212", False),
        ("990220472008213", False),
    ],
)
def test_identity_length(test_input, expected):
    assert expected == SouthAfricanIdentityValidate(test_input).identity_length()
