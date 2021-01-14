from za_id_number.za_identity_number import SouthAfricanIdentityValidate

validate_id = SouthAfricanIdentityValidate('9001245289086')

if __name__ == "__main__":
    print(validate_id.identity())