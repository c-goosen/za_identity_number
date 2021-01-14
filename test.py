from za_id_number.za_id_number import SouthAfricanIdentityValidate

validate_id = SouthAfricanIdentityValidate("9001245289086")

if __name__ == "__main__":
    print(validate_id.identity())
    print(validate_id.gender())
    print(validate_id.age())
    print(validate_id.birthdate())
