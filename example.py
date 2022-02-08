from za_id_number.za_id_number import (
    SouthAfricanIdentityValidate,
)
import logging

if __name__ == "__main__":
    logger = SouthAfricanIdentityValidate.get_logger(level=logging.DEBUG)
    # logger = logging.getLogger("za_id_number")
    # logger.removeHandler(logging.NullHandler())
    # logger.addHandler(logging.StreamHandler())
    za_validation = SouthAfricanIdentityValidate("9202204720082")
    valid = za_validation.validate()
    za_identity = za_validation.identity()
    logger.info(f"Valid: {valid}, Identity: {za_identity}")
    print(SouthAfricanIdentityValidate("99").identity_length())
