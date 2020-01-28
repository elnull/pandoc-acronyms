import unittest
from acronyms.index import Index
from acronyms.acronym import Acronym


class TestIndex(unittest.TestCase):
    def test_regoster(self):
        index = Index()
        a = Acronym('aba', 'ABA', 'A better acronym')
        count = index.register(a)
        self.assertEqual(count, 1)
        count = index.register(a)
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()
