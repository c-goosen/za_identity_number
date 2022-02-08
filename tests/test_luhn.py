import fast_luhn as luhn
from za_id_number.za_id_number import generate_random_number
import pytest


def test_luhn_validate():

    pos = luhn.validate("9001245289086")
    neg = luhn.validate("0000000000001")
    assert pos is True
    assert neg is False


def test_luhn_generate():
    luhn_gen = luhn.generate(20)
    assert len(luhn_gen) == 20
    assert luhn.validate(luhn_gen)


def test_luhn_complete():
    luhn_complete = luhn.complete("900124528908")
    assert luhn_complete == "9001245289086"
    assert luhn.validate(luhn_complete)


def test_luhn_digit():
    luhn_digit = luhn.digit("900124528908")
    assert luhn_digit == 6
    assert luhn.validate(f"900124528908{luhn_digit}")


@pytest.mark.parametrize(
    "test_input",
    [
        (1),
        (13),
        (23),
        (33),
    ],
)
def test_generate_random_number(test_input):
    assert len(generate_random_number(test_input)) == test_input
