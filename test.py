from za_id_number.za_id_number import (
    SouthAfricanIdentityValidate,
    SouthAfricanIdentityNumber,
)

if __name__ == "__main__":
    # Validation Class, inherits from Indentity Class
    validate_id = SouthAfricanIdentityValidate("9001245289086")
    # Class attributes
    print(validate_id.valid)
    # Other attributes are from identity Class
    # Functions
    print(validate_id.valid_birth_date())
    print(validate_id.validate())
    print(validate_id.identity())
    print(validate_id.identity_length())
    print("SouthAfricanIdentityValidate(0000000000000).validate()")
    print(SouthAfricanIdentityValidate("0000000000000").validate())
    print("Identity")

    # Identity Class
    identity_obj = SouthAfricanIdentityNumber("9001245289086")
    # Functions
    print(identity_obj.get_age())
    print(identity_obj.get_citizenship())
    print(identity_obj.get_gender())
    print(identity_obj.calculate_birthday())
    print(identity_obj.get_month())
    print(identity_obj.get_year())
    print(identity_obj.get_day())
    print(identity_obj.clean_input())

    # Class attributes
    print(identity_obj.id_number)
    print(identity_obj.birthdate)
    print(identity_obj.year)
    print(identity_obj.month)
    print(identity_obj.day)
    print(identity_obj.gender)
    print(identity_obj.citizenship)
    print(identity_obj.age)
