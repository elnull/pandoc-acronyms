import unittest
from tests.test_tools import return_local_test_data, convert_to_json
from acronyms.acronym_filter import Filter, run_acronyms_filter
import panflute
import io

class TestAcronymFilter(unittest.TestCase):
    def test_one_acronym(self):
        data = convert_to_json(return_local_test_data("one_acronym.md"))
        # migrate this into the filter class file:
        doc = panflute.load(io.StringIO(data))
        run_acronyms_filter(doc)
        # print(data)

    def test_is_match(self):
        filter = Filter()
        self.assertTrue(filter.is_match("[!BBA]"))
        self.assertFalse(filter.is_match("[!]"))
        self.assertFalse(filter.is_match("[]"))
        self.assertFalse(filter.is_match("[[!BBA]]"))
        self.assertFalse(filter.is_match("[@BBA]"))

if __name__ == '__main__':
    unittest.main()
