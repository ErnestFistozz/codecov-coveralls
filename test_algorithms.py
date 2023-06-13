import unittest
from algorithms import EncryptionAlgorithm, DencryptionAlgorithm


class TestAlgorithms(unittest.TestCase):

    def test_encryption(self):
        encrypt = EncryptionAlgorithm()
        self.assertEqual(encrypt.algorithm(1234), 189)
        self.assertEqual(encrypt.algorithm(123456), -1)
        self.assertEqual(encrypt.algorithm(9999), 6666)

    def test_decrpytion(self):
        decrypt = DencryptionAlgorithm()
        self.assertEqual(decrypt.algorithm(12345), 56347)
        self.assertEqual(decrypt.algorithm(12903), 12345)


if __name__ == '__main__':
    unittest.main()
