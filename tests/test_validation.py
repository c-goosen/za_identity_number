import pytest  # noqa
from za_id_number.za_id_number import SouthAfricanIdentityValidate
import datetime


def test_validation():
    validate = SouthAfricanIdentityValidate("9001245289086")
    assert validate.validate()


def test_identity():
    identity = SouthAfricanIdentityValidate("9001245289086").identity()
    assert identity["year"] == 1990
    assert identity["month"] == 1
    assert identity["day"] == 24
    assert identity["gender"] == "Male"
    assert identity["valid"]  # not actual ID number, example on website


def test_identity_types():
    identity = SouthAfricanIdentityValidate("9202204720082").identity()
    assert isinstance(identity, dict)
    assert isinstance(identity["gender"], str)
    assert isinstance(identity["year"], int)
    assert isinstance(identity["month"], int)
    assert isinstance(identity["day"], int)
    assert isinstance(identity["birthdate"], datetime.datetime)
    assert isinstance(identity["age"], int)


def test_validation_negative():
    validate = SouthAfricanIdentityValidate("9902204720089")
    assert not validate.validate()


def test_birthdate_elements():
    identity = SouthAfricanIdentityValidate("9902204720082").identity()
    assert identity["year"] != 1992
    assert identity["month"] != 3
    assert identity["day"] != 33


def test_identity_negative():
    identity = SouthAfricanIdentityValidate("9902204720082").identity()
    assert not identity["valid"]


def test_age():
    from dateutil.relativedelta import relativedelta
    year = '99'
    start_date = datetime.datetime.strptime(f"{year}-02-20", "%y-%m-%d")
    end_date = datetime.date.today()
    age = relativedelta(end_date, start_date).years
    assert SouthAfricanIdentityValidate(f"{year}02204720082").age() == age


def test_birthdate():
    birthdate = SouthAfricanIdentityValidate("9902204720082").birthdate()
    assert birthdate == datetime.datetime.strptime("99-02-20", "%y-%m-%d")


def test_all_zeroes():
    valid = SouthAfricanIdentityValidate("0000000000000").validate()
    assert valid


def test_alphabetical():
    valid = SouthAfricanIdentityValidate("123456ABC7890").validate()
    assert not valid

@pytest.mark.parametrize("test_input,expected", [
    ("0000000000000", True),
    ("0000000000001", False),
    ("0010000000000", False),
    ("00100000000001", False),
]
                         )
def test_edge_cases_validate(test_input, expected):
    assert expected == SouthAfricanIdentityValidate(test_input).validate()

def test_github_issue_4():
    valid = SouthAfricanIdentityValidate("0000000000000").validate()
    assert valid