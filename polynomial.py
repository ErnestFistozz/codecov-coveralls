from math import sqrt


class Quadratic:

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self) -> float:
        return pow(self.b, 2)-4*self.a*self.c

    def roots(self) -> tuple:
        x1, x2 = 0, 0

        if self.discriminant() > 0:
            x1, x2 = round((-self.b + sqrt(self.discriminant()))/2 *
                           self.a, 3), round((-self.b - sqrt(self.discriminant()))/2*self.a, 3)
        elif self.discriminant() == 0:
            x1 = x2 = round(-self.b / (self.a * 2), 3)
        else:
            x11 = x21 = -self.b / (self.a * 2)
            x12 = " + j" + str(
                round((sqrt(-1*self.discriminant()))/2*self.a, 3))
            x22 = " - j" + \
                str(round((sqrt(-1*self.discriminant()))/2*self.a, 3))
            x1 = str(x11) + x12
            x2 = str(x21) + x22
        return x1, x2


if __name__ == '__main__':
    print(__name__)
