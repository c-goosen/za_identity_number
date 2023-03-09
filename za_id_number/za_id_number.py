from datetime import date, datetime, timedelta
import random

import luhn
from za_id_number.constants import (
    Gender,
    CitizenshipClass,
    LIB_DATE_FORMAT,
    LIB_ID_DATE_FORMAT,
)
from functools import lru_cache
import logging


# logger = logging.getLogger().isEnabled(level)
# Since this is a library we immediately disable logging.
# If logging within the library is desired, then add a handler to the logger
# or call SouthAfricanIdentityValidate.get_logger(level=logging.DEBUG)
logger = logging.getLogger("za_id_number")
logger.addHandler(logging.NullHandler())
# from within your script.
# logger = SouthAfricanIdentityValidate.get_logger(level=logging.DEBUG)
# logger.debug("Hello")


def check_length(f):
    def wrapper(*args):
        logger.debug(args[0].id_number)
        return f(*args)

    return wrapper


class SouthAfricanIdentityNumber(object):
    """
    Identity Number Class.
    Validates and sets up Identity Number class object
    """

    def __init__(self, id_number: str):
        self.id_number: str = id_number
        self.length_valid = True if len(id_number) == 13 else False
        self.clean_input()
        self.birthdate: datetime = self.calculate_birthday()
        self.year = self.get_year()
        self.month = self.get_month()
        self.day = self.get_day()
        self.gender = self.get_gender()
        self.citizenship = self.get_citizenship()
        self.age = self.get_age()

    @staticmethod
    def get_logger(level=logging.DEBUG):
        """
        Helper for quickly adding a StreamHandler to the logger. Useful for
        debugging. Logger not on by default

        Returns the handler after adding it.
        """
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("[%(asctime)s] [%(module)s] [%(levelname)s]: %(message)s")
        )
        logger.addHandler(handler)
        logger.setLevel(level)
        logger.debug(f"Added a {level} logging handler to logger: %s", __name__)
        return logger

    @lru_cache(100)
    def identity_length(self) -> bool:
        """
        Test identity number is 13 characters
        """
        if len(str(self.id_number)) != 13:
            return False
        else:
            return True

    def clean_input(self):
        self.id_number = self.id_number.strip()

    def get_day(self):
        return self.birthdate.day if self.birthdate else None

    def get_year(self):
        if self.birthdate:
            return self.birthdate.year if self.birthdate else None

    def get_month(self) -> int:
        if self.birthdate:
            return self.birthdate.month if self.birthdate else None

    @lru_cache(100)
    def calculate_birthday(self):
        try:
            datetime_obj = datetime.strptime(
                f"{self.id_number[:2]}-{self.id_number[2:4]}-{self.id_number[4:6]}",
                LIB_DATE_FORMAT,
            )
            if datetime_obj > datetime.now():
                return datetime_obj.replace(year=(datetime_obj.year - 100)).date()
            return datetime_obj.date()

        except ValueError as e:
            logger.error(e)
            return None

    def get_gender(self) -> str:
        try:
            gen_num = int(self.id_number[6:10])
            logger.debug(f"gen_num {gen_num}")
            if gen_num < 5000:
                return Gender.FEMALE.value
            else:
                return Gender.MALE.value

        except ValueError as e:
            logger.error(e)
            return None

    def get_citizenship(self):
        """
        Citizen or resident.
        Only these two classes of people can receive an ID number
        """
        try:
            citizen_num = int(self.id_number[10])
            return (
                CitizenshipClass.CITIZEN_BORN.value
                if citizen_num == 0
                else CitizenshipClass.CITIZEN_NOT_BORN.value
            )
        except Exception as e:
            logger.error(e)
            return False

    @lru_cache(100)
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
        except Exception as e:
            logger.error(e)
            return None


class SouthAfricanIdentityValidate(SouthAfricanIdentityNumber):
    def __init__(self, id_number: str):
        # super(SouthAfricanIdentityValidate, self).__init__(id_number)
        super().__init__(id_number)
        self.valid = self.validate()

    @lru_cache(100)
    def valid_birth_date(self) -> bool:
        """
        Ensures that birthday is a valid date.
        A test case for this is the ID number 0000000000000
        00-00-00 is not a valid date.
        """
        try:
            if self.calculate_birthday():
                return True
            else:
                return False
        except Exception as e:
            logger.error(e)
            return True

    def validate(self) -> bool:
        """
        Valid ID or not?
        Luhn algorithm validates the ID number
        Additional check is where the date makes sense
        In Luhn 0000
        """
        if self.identity_length() and self.valid_birth_date():
            try:
                return bool(luhn.verify(self.id_number))
            except ValueError as e:
                logger.error(e)
                return False
        else:
            return False

    def identity(self) -> dict:
        """
        Return dict of identity
        Class to dict
        """
        # return self.__dict__
        if self.identity_length():
            return self.__dict__
        else:
            return {}


class SouthAfricanIdentityGenerate(SouthAfricanIdentityValidate):
    def __init__(self, gender=None, citizenship=None):
        # super(SouthAfricanIdentityValidate, self).__init__(id_number)
        id_number = self.generate(gender=gender, citizenship=citizenship)
        super().__init__(id_number)

    @staticmethod
    def generate_date():
        time_between_dates = date.today() - date(1900, 1, 1)
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = date.today() + timedelta(days=random_number_of_days)
        return random_date.strftime(LIB_ID_DATE_FORMAT)

    @staticmethod
    def generate_gender(gender=None):
        if gender:
            if gender in ["female", "f", Gender.FEMALE]:
                logger.debug("hit F")
                min = 0
                max = 5000
            elif gender in ["male", "m", Gender.MALE]:
                logger.debug("hit M")
                min = 5000
                max = 10000
        else:
            logger.debug("hit if")
            min = 0
            max = 10000
        rand_int = random.randrange(min, max)
        rand_int = f"{rand_int:04d}"
        logger.debug(rand_int)
        return rand_int

    @staticmethod
    def generate_citizenship(citizenship=None):

        if not citizenship:
            random_choice = random.choice([f"{0:01d}", f"{1:01d}"])
            logger.debug(f"random_choice {random_choice}")
            return random_choice
        else:
            if citizenship in ["citizen", CitizenshipClass.CITIZEN_BORN]:
                return f"{0:01d}"
            elif citizenship in ["resident", CitizenshipClass.CITIZEN_NOT_BORN]:
                return f"{1:01d}"

    @classmethod
    def generate(cls, gender=None, citizenship=None):
        _date = cls.generate_date()
        _gender = cls.generate_gender(gender=gender)
        _citizenship = cls.generate_citizenship(citizenship=citizenship)
        _race_deprecated = 8
        _luhn_nr = luhn.append(f"{_date}{_gender}{_citizenship}{_race_deprecated:01d}")
        logger.debug(_luhn_nr)
        logger.debug(f"len {len(_luhn_nr)}")
        return _luhn_nr


def generate_random_id(gender=None, citizenship=None):
    return SouthAfricanIdentityGenerate.generate(gender=gender, citizenship=citizenship)
