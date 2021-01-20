# za_identity_number
Library to validate/check and retrieve ID number info for South African IDs

Current version: 0.0.3

Poetry & pip compatibility

Python 3.5 or greater for f-strings

Installation:

pip:
```buildoutcfg

pip install za-id-number

```

poetry:

```buildoutcfg

poetry add za-id-number

```

ZA Id Numbers:

ZA id  numbers are based on a luhn algorithm validation, with the last number validating that the entire number is correct.

ZA ID number is broken up into  2 digits birth year, 2 digits birth month, 2 digits birth date, 4 digits for gender, 1 digit for citizenship (za/other), 1 digit race (phased out after 1980) 1 digit for validation.

For more info: https://www.westerncape.gov.za/sites/www.westerncape.gov.za/files/sa-id-number-new.png

Easiest ZA ID validation is the length. The length must be exactly 13 integers.

Example:
```
from za_id_number.za_identity_number import SouthAfricanIdentityValidate

if __name__ == "__main__":
    za_validation = SouthAfricanIdentityValidate("9202204720082")
    valid = za_validation.validate()
    za_identity = za_validation.identity()
    print(f"Valid: {valid}, Identity: {za_identity}")
```

Methods:
```
SouthAfricanIdentityValidate("9202204720082").validate()
SouthAfricanIdentityValidate("9202204720082").identity()
SouthAfricanIdentityValidate("9202204720082").gender()
SouthAfricanIdentityValidate("9202204720082").citizen()
SouthAfricanIdentityValidate("9202204720082")identity_length()
SouthAfricanIdentityValidate("9202204720082").age()


```