from za_id_number.za_id_number import (
    SouthAfricanIdentityValidate,
    SouthAfricanIdentityNumber,
)
from luhn import verify

validate_id = SouthAfricanIdentityValidate("9001245289086")
identity_obj = SouthAfricanIdentityNumber("9001245289086")

if __name__ == "__main__":
    print(validate_id.identity())
    print(validate_id.gender())
    print(validate_id.age())
    print(validate_id.birthdate())
    print("SouthAfricanIdentityValidate(0000000000000).validate()")
    print(SouthAfricanIdentityValidate("0000000000000").validate())
    print("Identity")

    print(identity_obj.is_datetime(identity_obj.birthdate))
    print(identity_obj.birthdate)
    print(identity_obj.year)
    print(identity_obj.get_year())
    print(identity_obj.calculate_birthday())
    print("Luhn")
    print(verify("0000000000000"))
