import unittest
from identity_validator import IdentiyValidator


class TestIdentityVerifier(unittest.TestCase):
    def test_gender(self):
        m_id = IdentiyValidator("9205235008089")
        f_id = IdentiyValidator("9205234008089")
        self.assertEqual(m_id.identify_gender(), 'Male')
        self.assertEqual(f_id.identify_gender(), 'Female')

    def test_citizenship(self):
        rsa = IdentiyValidator("9205235008089")
        perm_res = IdentiyValidator("9205234008189")
        self.assertEqual(rsa.citizenship(), 'South African')
        self.assertEqual(perm_res.citizenship(), 'Permanent Resident')

    def check_validity(self):
        id = IdentiyValidator("9999998548598")
        self.assertEqual(id.valid_identity(), False)


if __name__ == '__main__':
    unittest.main()
