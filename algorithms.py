

class EncryptionAlgorithm:
    def algorithm(self, number: int) -> int:
        value = str(number)
        if len(value) != 4 or not value.isdigit():
            return -1
        first_step = [str((int(i)+7) % 10) for i in value]
        first_step[0], first_step[2] = first_step[2], first_step[0]
        first_step[1], first_step[3] = first_step[3], first_step[1]

        if len("".join(first_step)) != 4:
            return -1
        return int("".join(first_step))


class DencryptionAlgorithm:
    def algorithm(self, number: int) -> int:
        value = str(number)
        if len(value) != 5 or not value.isdigit():
            return -1
        first_step = list(value)
        first_step[1], first_step[3] = first_step[3], first_step[1]
        first_step[0], first_step[2] = first_step[2], first_step[0]
        result = [str((int(i)+2) % 10) for i in first_step]
        if len("".join(result)) != 5:
            return -1
        return int("".join(result))


if __name__ == '__main__':
    print(__name__)
