from datetime import date, datetime
from luhn import verify
from functools import lru_cache


class SouthAfricanIdentityValidate(object):
    def __init__(self, id_number):
        self.id_number = id_number

    def validate(self):
        if self.identity_length():
            return SouthAfricanIdentityNumber(self.id_number).valid
        else:
            return False

    def identity(self):
        if self.identity_length():
            return SouthAfricanIdentityNumber(self.id_number).__dict__
        else:
            return dict()

    def identity_length(self) -> bool:
        if len(str(self.id_number)) != 13:
            return False
        else:
            return True

    def gender(self) -> str:
        return SouthAfricanIdentityNumber(self.id_number).gender

    def age(self) -> int:
        return SouthAfricanIdentityNumber(self.id_number).age

    def birthdate(self) -> datetime:
        return SouthAfricanIdentityNumber(self.id_number).birthdate


class SouthAfricanIdentityNumber(object):
    """
    Identity Number Class.
    Validates and sets up Identity Number class object
    """

    def __init__(self, id_number):
        self.id_number = id_number
        self.valid = self.validate()
        self.birthdate = self.calculate_birthday()
        self.year = self.get_year()
        self.month = self.get_month()
        self.day = self.get_day()
        self.gender = self.gender()
        self.citizenship = self.citizen()
        self.age = self.age()

    def get_year(self):
        if self.is_datetime(self.birthdate):
            return self.birthdate.year
        else:
            return None

    def get_month(self):
        return (self.birthdate.month if self.is_datetime(self.birthdate) else None)

    def get_day(self):
        return (self.birthdate.day if self.is_datetime(self.birthdate) else None)

    @lru_cache
    def is_datetime(self, birthdate):
        return True if birthdate else False

    def calculate_birthday(self):
        try:
            datetime.strptime(
            f"{self.id_number[:2]}-{self.id_number[2:4]}-{self.id_number[4:6]}", "%y-%m-%d"
            )
            print(f"datetime.strptime {datetime.strptime}")
        except Exception:
            return None

    def validate(self) -> bool:
        return bool(verify(self.id_number))

    def identity_dict(self) -> dict:
        return self.__dict__

    def gender(self):
        gen_num = int(self.id_number[6:9])
        if gen_num <= 4999:
            return "Male"
        else:
            return "Female"

    def citizen(self):
        citizen_num = int(self.id_number[10])
        return True if citizen_num == 0 else False

    def age(self):
        if self.is_datetime(self.birthdate):
            today = date.today()
            age = (today.year - self.birthdate.year) - (
                1
                if ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
                else 0
            )
            return int(age)
        else:
            return None
