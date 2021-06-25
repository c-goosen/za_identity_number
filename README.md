# za_identity_number
ZA / RSA Identity Number 
Library to validate/check/manipulate and retrieve ID number info for South African IDs

Current version: 0.0.4-3 

Poetry & pip compatibility

Python 3.5 or greater for f-strings

Installation:

pip:
```bash

pip install za-id-number

```

poetry:

```bash

poetry add za-id-number

```

ZA ID Numbers / RSA ID numbers / South African ID numbers:

ZA id numbers are validated by the luhn algorithm, with the last number validating that the entire number is correct.

ZA ID number is broken up into  2 digits birth year, 2 digits birth month, 2 digits birth date, 4 digits for gender, 1 digit for citizenship (za/other), 1 digit race (phased out after 1980) 1 digit for validation.

For more info: https://www.westerncape.gov.za/sites/www.westerncape.gov.za/files/sa-id-number-new.png

Easiest ZA ID validation is the length. The length must be exactly 13 integers.

Example:
```python
from za_id_number.za_identity_number import SouthAfricanIdentityValidate

if __name__ == "__main__":
    za_validation = SouthAfricanIdentityValidate("9202204720082")
    valid = za_validation.validate()
    za_identity = za_validation.identity()
    print(f"Valid: {valid}, Identity: {za_identity}")
```

Classes:
```python
# Validation class, inherits from SouthAfricanIdentityNumber
validate_id = SouthAfricanIdentityValidate("9001245289086")

# SouthAfricanIdentityNumber class
identity_obj = SouthAfricanIdentityNumber("9001245289086")
```

Class Attributes:
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

Methods:
```python
# SouthAfricanIdentityValidate class
SouthAfricanIdentityValidate("9202204720082").valid_birth_date()
SouthAfricanIdentityValidate("9202204720082").validate()
SouthAfricanIdentityValidate("9202204720082").identity()
SouthAfricanIdentityValidate("9202204720082").identity_length()

# SouthAfricanIdentityNumber class
SouthAfricanIdentityNumber("9202204720082").get_age()
SouthAfricanIdentityNumber("9202204720082").get_citizenship()
SouthAfricanIdentityNumber("9202204720082").get_gender()
SouthAfricanIdentityNumber("9202204720082").calculate_birthday()
SouthAfricanIdentityNumber("9202204720082").get_month()
SouthAfricanIdentityNumber("9202204720082").get_year()
SouthAfricanIdentityNumber("9202204720082").get_day()


```

Questions/Ideas/Feedback

christogoosen@gmail.com
christo@anomaloustech.co.za

Future features:
* Generating random ID numbers