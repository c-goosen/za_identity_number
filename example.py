from za_id_number.za_id_number import (
    SouthAfricanIdentityValidate,
)

if __name__ == "__main__":
    za_validation = SouthAfricanIdentityValidate("9202204720082")
    valid = za_validation.validate()
    za_identity = za_validation.identity()
    print(f"Valid: {valid}, Identity: {za_identity}")
