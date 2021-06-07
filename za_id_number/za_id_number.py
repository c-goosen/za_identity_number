from datetime import date, datetime

from luhn import verify
from za_id_number.constants import Gender, Citizen

from functools import lru_cache


class SouthAfricanIdentityNumber(object):
    """
    Identity Number Class.
    Validates and sets up Identity Number class object
    """

    def __init__(self, id_number: str):
        self.id_number: str = id_number
        self.birthdate: datetime = self.calculate_birthday()
        self.year = self.get_year()
        self.month = self.get_month()
        self.day = self.get_day()
        self.gender = self.get_gender()
        self.citizenship = self.get_citizenship()
        self.age = self.get_age()

    def get_day(self):
        return self.birthdate.day if self.birthdate else None

    def get_year(self):
        if self.birthdate:
            return self.birthdate.year if self.birthdate else None

    def get_month(self) -> int:
        if self.birthdate:
            return self.birthdate.month if self.birthdate else None

    def calculate_birthday(self):
        try:
            return datetime.strptime(
                f"{self.id_number[:2]}-{self.id_number[2:4]}-{self.id_number[4:6]}",
                "%y-%m-%d",
            )

        except ValueError:
            return None

    def get_gender(self) -> str:
        try:
            gen_num = int(self.id_number[6:9])
            if gen_num <= 4999:
                return Gender.MALE.value
            else:
                return Gender.FEMALE.value
        except Exception:
            return None

    def get_citizenship(self):
        """
        Needs work
        TODO: Resident vs born citizen
        """
        try:
            citizen_num = int(self.id_number[10])
            return True if citizen_num == 0 else False
        except Exception:
            return None

    def get_age(self) -> int:
        try:
            today = date.today()
            age = (today.year - self.birthdate.year) - (
                1
                if (
                    (today.month, today.day)
                    < (self.birthdate.month, self.birthdate.day)
                )
                else 0
            )
            return int(age)
        except Exception:
            return None


class SouthAfricanIdentityValidate(SouthAfricanIdentityNumber):
    def __init__(self, id_number):
        # super(SouthAfricanIdentityValidate, self).__init__(id_number)
        super().__init__(id_number)
        self.valid = self.validate()

    @lru_cache
    def valid_birth_date(self) -> bool:
        try:
            if self.calculate_birthday():
                return True
            else:
                return False
        except Exception:
            return True

    def validate(self) -> bool:
        if self.identity_length() and self.valid_birth_date():
            try:
                return bool(verify(self.id_number))
            except ValueError:
                return False
        else:
            return False

    def identity(self) -> dict:
        # return self.__dict__
        if self.identity_length():
            return self.__dict__
        else:
            return {}

    def identity_length(self) -> bool:
        if len(str(self.id_number)) != 13:
            return False
        else:
            return True
