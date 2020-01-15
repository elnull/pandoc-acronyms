import unittest
from acronyms.Acronym import Acronym

class TestAcronym(unittest.TestCase):

    def test_setget(self):
        a = Acronym()
        self.assertEqual(a.key, '')
        a.key = 1
        self.assertIsInstance(a.key, str, "Acronym keys should be converted to strings.")
        self.assertEqual(a.key, '1')

if __name__ == '__main__':
    unittest.main()