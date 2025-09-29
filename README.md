# za_identity_number

ZA / RSA Identity Number 
Library to validate/check/manipulate and retrieve ID number info for South African IDs

Current version: 0.2.0

Downloads total:  [![Downloads](https://static.pepy.tech/personalized-badge/za-id-number?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/za-id-number)

UV & pip compatibility

Python 3.5 or greater for f-strings.
Officially only support from py 3.7 >=

Python3.12 support added in CI

# Installation:

pip:
```bash

pip install za-id-number

```

uv:

```bash

uv add za-id-number

```

ZA ID Numbers / RSA ID numbers / South African ID numbers:

ZA id numbers are validated by the luhn algorithm, with the last number validating that the entire number is correct.

ZA ID number is broken up into  2 digits birth year, 2 digits birth month, 2 digits birth date, 4 digits for gender, 1 digit for citizenship (za/other), 1 digit race (phased out after 1980) 1 digit for validation.

For more info: https://www.westerncape.gov.za/sites/www.westerncape.gov.za/files/sa-id-number-new.png

Easiest ZA ID validation is the length. The length must be exactly 13 integers.

# Example:
```python
from za_id_number.za_id_number import SouthAfricanIdentityValidate

if __name__ == "__main__":
    za_validation = SouthAfricanIdentityValidate("9202204720082")
    valid = za_validation.validate()
    za_identity = za_validation.identity()
    print(f"Valid: {valid}, Identity: {za_identity}")
```
# Logging
As its a library logging is off by default.
To get a logger for the library you can use the following example:
```python
    logger = SouthAfricanIdentityValidate.get_logger(level=logging.DEBUG)
    # logger = logging.getLogger("za_id_number")
    # logger.removeHandler(logging.NullHandler())
    # logger.addHandler(logging.StreamHandler())
    za_validation = SouthAfricanIdentityValidate("9202204720082")
    valid = za_validation.validate()
    za_identity = za_validation.identity()
    logger.info(f"Valid: {valid}, Identity: {za_identity}")
    print(SouthAfricanIdentityValidate("99").identity_length())
```

# Classes:
```python
# Validation class, inherits from SouthAfricanIdentityNumber
validate_id_obj = SouthAfricanIdentityValidate("9001245289086")

# SouthAfricanIdentityNumber class
identity_obj = SouthAfricanIdentityNumber("9001245289086")

# SouthAfricanIdentityGenerate class
generated_id_obj = SouthAfricanIdentityGenerate()
```

# Class Attributes:
```python
# SouthAfricanIdentityValidate
SouthAfricanIdentityValidate("9202204720082").valid

# SouthAfricanIdentityNumber
SouthAfricanIdentityNumber("9202204720082").id_number
SouthAfricanIdentityNumber("9202204720082").birthdate
SouthAfricanIdentityNumber("9202204720082").year
SouthAfricanIdentityNumber("9202204720082").month
SouthAfricanIdentityNumber("9202204720082").day
SouthAfricanIdentityNumber("9202204720082").gender
SouthAfricanIdentityNumber("9202204720082").citizenship
SouthAfricanIdentityNumber("9202204720082").age

```

# Methods:
```python
# SouthAfricanIdentityNumber class
SouthAfricanIdentityNumber("9202204720082").get_age()
SouthAfricanIdentityNumber("9202204720082").get_citizenship()
SouthAfricanIdentityNumber("9202204720082").get_gender()
SouthAfricanIdentityNumber("9202204720082").calculate_birthday()
SouthAfricanIdentityNumber("9202204720082").get_month()
SouthAfricanIdentityNumber("9202204720082").get_year()
SouthAfricanIdentityNumber("9202204720082").get_day()


# SouthAfricanIdentityValidate class
# Inherits from SouthAfricanIdentityNumber
# All attributes and methods available
SouthAfricanIdentityValidate("9202204720082").valid_birth_date()
SouthAfricanIdentityValidate("9202204720082").validate()
SouthAfricanIdentityValidate("9202204720082").identity()
SouthAfricanIdentityValidate("9202204720082").identity_length()

# SouthAfricanIdentityGenerate class
# Inherits from SouthAfricanIdentityValidate
# All attributes and methods available
# gender and citizenship can be specified for specific random
# id numbers
SouthAfricanIdentityGenerate()
# or
SouthAfricanIdentityGenerate(gender="male", citizenship='citizen')
# or
from za_id_number.constants import Gender, CitizenshipClass
SouthAfricanIdentityGenerate(gender=Gender.FEMALE, citizenship=CitizenshipClass.CITIZEN_BORN)
# generate random ID number without using class obj
generate_random_id()

```

Questions/Ideas/Feedback

christogoosen@gmail.com
christo@anomaloustech.co.za

## Future features:
* Ask for some please

## CI/CD
Covers python:
* 3.9
* 3.10
* 3.11
* 3.12
* 3.13
Check CI: https://github.com/c-goosen/za_identity_number/actions

Keeping up with python release cycle: https://devguide.python.org/versions/

# Releases:
* 0.0.7
  * Upgrade packages idenitified by github security scanning
  * Remove loguru
  * Disable loggin in library by default
  * Fixed some exceptions
  * Removed luhn library for fast-luhn
  * fast-luhn adds generate and complete functions
  * Generate Random ID numbers
  * Generate random luhn numbers of length n
* 0.0.8
  * Removed fast-luhn library as pyo3 rust implementation not building for Mac or python greater than 3.8
  * Simplified library.
  * Security issues in dependencies updated
* 0.0.9
  * Add python 3.12 to CI
  * Security updates in dependencies
* 0.1.0
  * Deprecated python versions below 3.9
  * Update dependencies
