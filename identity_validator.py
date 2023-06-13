ID_SIZE = 13


class InvalidRSAIndetifier(Exception):
    pass


class IdentiyValidator:

    def __init__(self, identity_number: str) -> None:
        try:
            if len(identity_number) > ID_SIZE or len(identity_number) < ID_SIZE and not identity_number.isdigit():
                raise InvalidRSAIndetifier
            self.identity_no = identity_number

        except InvalidRSAIndetifier:
            print('invalid id provided')

    def citizenship(self) -> str:
        match(int(self.identity_no[10])):
            case 0:
                return 'South African'
            case 1:
                return 'Permanent Resident'
            case _:
                return

    def identify_gender(self) -> str:
        return 'Female' if int(self.identity_no[6:10]) <= 4999 else 'Male'

    def valid_identity(self) -> bool:
        birth_month, birth_day = int(
            self.identity_no[2:4]), int(self.identity_no[4:6])

        valid_month = True if (
            birth_month >= 1 and birth_month <= 12) else False
        valid_day = True if (birth_day >= 1 and birth_day <= 31) else False
        print("Valid day: ", valid_day)
        print("Valid day: ", valid_month)
        if len(self.identity_no) != ID_SIZE or not self.identity_no.isdigit() or not valid_month or not valid_day:
            return False
        return True


if __name__ == '__main__':
    print(__name__)
