from za_id_number.za_id_number import (
    SouthAfricanIdentityValidate,
    SouthAfricanIdentityGenerate,
    generate_random_id,
)
from za_id_number.constants import Gender, CitizenshipClass
import pytest  # noqa


def test_generate_random_id():
    test_id = generate_random_id()
    assert SouthAfricanIdentityValidate(test_id).validate()


def test_SouthAfricanIdentityGenerate():
    generated_id_obj = SouthAfricanIdentityGenerate()
    assert len(generated_id_obj.id_number) == 13
    assert generated_id_obj.length_valid
    assert generated_id_obj.validate()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("m", Gender.MALE.value),
        (Gender.MALE, Gender.MALE.value),
        ("male", Gender.MALE.value),
        ("f", Gender.FEMALE.value),
        ("female", Gender.FEMALE.value),
        (Gender.FEMALE, Gender.FEMALE.value),
    ],
)
def test_SouthAfricanIdentityGenerate_gender(test_input, expected):
    generated_id_obj = SouthAfricanIdentityGenerate(gender=test_input)
    assert len(generated_id_obj.id_number) == 13
    assert generated_id_obj.length_valid
    assert generated_id_obj.validate()
    assert generated_id_obj.gender == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("citizen", CitizenshipClass.CITIZEN_BORN.value),
        (CitizenshipClass.CITIZEN_BORN, CitizenshipClass.CITIZEN_BORN.value),
        ("resident", CitizenshipClass.CITIZEN_NOT_BORN.value),
        (CitizenshipClass.CITIZEN_NOT_BORN, CitizenshipClass.CITIZEN_NOT_BORN.value),
    ],
)
def test_SouthAfricanIdentityGenerate_citizenship(test_input, expected):
    generated_id_obj = SouthAfricanIdentityGenerate(citizenship=test_input)
    assert len(generated_id_obj.id_number) == 13
    assert generated_id_obj.length_valid
    assert generated_id_obj.validate()
    assert generated_id_obj.citizenship == expected
