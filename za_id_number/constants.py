from enum import Enum

"""
Constants from:
https://www.westerncape.gov.za/general-publication/decoding-your-south-african-id-number-0

"""

LIB_DATE_FORMAT = "%y-%m-%d"


class Gender(Enum):
    """
    The next 4 digits (SSSS) are used to define your gender.  Females are assigned numbers in the range 0000-4999
    and males from 5000-9999.
    """

    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class CitizenshipClass(Enum):
    """
    The next digit (C) shows if you're an SA citizen status with 0 denoting that you were born a SA citizen and 1
    denoting that you're a permanent resident.
    """

    CITIZEN_BORN = "South African Citizen"
    CITIZEN_NOT_BORN = "Permanent resident"
    NONCITIZEN = "Not a RSA Citizen"

