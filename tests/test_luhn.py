import luhn
import pytest  # noqa


def test_luhn_validate():

    pos = luhn.verify("9001245289086")
    neg = luhn.verify("0000000000001")
    assert pos is True
    assert neg is False


# def test_luhn_generate():
#     luhn_gen = luhn.generate(20)
#     assert len(luhn_gen) == 20
#     assert luhn.verify(luhn_gen)


def test_luhn_complete():
    luhn_complete = luhn.append("900124528908")
    assert luhn_complete == "9001245289086"
    assert luhn.verify(luhn_complete)


def test_luhn_digit():
    luhn_digit = luhn.generate("900124528908")
    assert luhn_digit == 6
    assert luhn.verify(f"900124528908{luhn_digit}")
