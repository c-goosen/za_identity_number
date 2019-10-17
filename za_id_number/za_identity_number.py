from luhn import verify


class SouthAfricanIdentityValidate(object):
    def __init__(self, id_number):
        self.id_number = id_number

    def validate(self):
        if self.identity_length():
            return SouthAfricanIdentityNumber(self.id_number).valid
        else:
            return False

    def identity(self):
        if self.identity_length():
            return SouthAfricanIdentityNumber(self.id_number).__dict__
        else:
            return dict()

    def identity_length(self) -> bool:
        if len(str(self.id_number)) != 13:
            return False
        else:
            return True

class SouthAfricanIdentityNumber(object):
    """
    Identity Number Class.
    Validates and sets up Identity Number class object
    """

    def __init__(self, id_number):
        self.id_number = id_number
        self.year = id_number[:2]
        self.month = id_number[2:4]
        self.day = id_number[4:6]
        self.gender = self.gender()
        self.citizenship = self.citizen()
        self.valid = self.validate()

    def validate(self) -> bool:

        return bool(verify(self.id_number))

    def identity_dict(self) -> dict:

        return self.__dict__

    def gender(self):
        gen_num = int(self.id_number[6:9])
        if gen_num <= 4999:
            return "Male"
        else:
            return "Female"

    def citizen(self):
        citizen_num = int(self.id_number[10])
        return True if citizen_num == 0 else False


if __name__ == "__main__":
    val = SouthAfricanIdentityValidate("9202204720082")
    print(val.validate())
    print(val.identity())

