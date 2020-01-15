import unittest
from acronyms.acronyms import Acronyms
from acronyms.acronym import Acronym

class TestAcronyms(unittest.TestCase):
    def test_acronyms(self):
        acronyms = Acronyms()
        self.assertEqual(len(acronyms.values), 0)
        a = Acronym('aba', 'ABA', 'A Better Acronym')
        b = Acronym('bba', 'BBA', 'Beer Brewing Attitude')
        acronyms.set(a)
        acronyms.set(b)
        self.assertEqual(len(acronyms.values), 2)
        self.assertEqual(acronyms.get(a.key), a)
        self.assertEqual(acronyms.get(b.key), b)
        self.assertEqual(acronyms.get('nonsense'), None)

if __name__ == '__main__':
    unittest.main()
