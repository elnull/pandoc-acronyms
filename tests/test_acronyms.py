import unittest
import os
import tempfile
from acronyms.acronyms import Acronyms
from acronyms.acronym import Acronym
from tests.test_tools import return_local_test_data


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

    def test_read(self):
        with open(return_local_test_data("two_basic_acronyms.json"), "r") as handle:
            a = Acronyms.Read(handle)
            self.assertEqual(len(a.values), 2)
            aba = a.get('aba')
            self.assertEqual(aba.shortform, 'ABA')
            self.assertEqual(aba.longform, 'a better acronym')
            aba = a.get('bba')
            self.assertEqual(aba.shortform, 'BBA')
            self.assertEqual(aba.longform, 'beer brewing attitude')

    def test_read_incomplete_entries(self):
        with open(return_local_test_data("incomplete_acronyms.json"), "r") as handle:
            a = Acronyms.Read(handle)
            self.assertEqual(len(a.values), 3)
            shortonly = a.get('shortonly')
            self.assertEqual(shortonly.shortform, 'so')
            self.assertEqual(shortonly.longform, '')

    def test_write_read(self):
        a = Acronyms()
        with open(return_local_test_data("two_basic_acronyms.json"), "r") as handle:
            a = Acronyms.Read(handle)
            self.assertEqual(len(a.values), 2)
        tmp_file_path = ""
        with tempfile.NamedTemporaryFile(prefix='python-test-', suffix='.json', delete=False) as file:
            tmp_file_path = file.name
            a.write(file)
        with open(tmp_file_path, "r") as handle:
            b = Acronyms.Read(handle)
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
