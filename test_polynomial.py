import unittest
from polynomial import Quadratic


class TestPolynomial(unittest.TestCase):

    def test_positive_discriminat(self):
        poly = Quadratic(1, -2, -3)
        x1, x2 = poly.roots()
        self.assertEqual(x1, 3.0)
        self.assertEqual(x2, -1.0)

        poly2 = Quadratic(1, 1, -4)
        x11, x22 = poly2.roots()
        self.assertEqual(x11, 1.562)
        self.assertEqual(x22, -2.562)

    def test_zero_discriminat(self):
        poly = Quadratic(1, 2, 1)
        x1, x2 = poly.roots()
        self.assertEqual(x1, -1.0)
        self.assertEqual(x2, -1.0)

    def test_negative_discriminat(self):
        poly = Quadratic(1, 1, 0.5)
        x1, x2 = poly.roots()
        self.assertEqual(x1, "-0.5 + j0.5")
        self.assertEqual(x2, "-0.5 - j0.5")

        poly2 = Quadratic(1, 0, 0.5)
        x11, x22 = poly2.roots()
        self.assertEqual(x11, "0.0 + j0.707")
        self.assertEqual(x22, "0.0 - j0.707")


if __name__ == '__main__':
    unittest.main()
