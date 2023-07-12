import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_name(self):
        per1 = Person('John', 'Doe')
        self.assertEqual('John', per1.name)

    def test_surname(self):
        per2 = Person('John', 'Doe')
        self.assertEqual('Doe',per2.surname)

if __name__ == '__main__':
    unittest.main()