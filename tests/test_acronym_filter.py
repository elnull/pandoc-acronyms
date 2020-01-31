import unittest
from tests.test_tools import return_local_test_data, convert_to_json
from acronyms.acronym_filter import Filter
from acronyms.acronyms import Acronyms
import panflute
import io


class TestAcronymFilter(unittest.TestCase):
    def test_one_acronym(self):
        doc = self._loadJSONDocument("one_acronym.md")
        filter = Filter()
        filter.acronyms = self._createAcronymsDictionary(
            "two_basic_acronyms.json")
        filter.process_document(doc)
        self.assertEqual(filter.index.occurences('bba'), 1)
        self.assertEqual(filter.index.occurences('aba'), 0)

    def test_is_match(self):
        filter = Filter()
        self.assertTrue(filter.is_match("[!BBA]"))
        self.assertFalse(filter.is_match("[!]"))
        self.assertFalse(filter.is_match("[]"))
        self.assertFalse(filter.is_match("[[!BBA]]"))
        self.assertFalse(filter.is_match("[@BBA]"))

    def test_run_method(self):
        doc = self._loadJSONDocument("one_acronym.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        try:
            filter.run([acronyms], doc)
        except:
            self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 1)

    def test_run_method_no_acronymns(self):
        doc = self._loadJSONDocument("one_acronym.md")
        filter = Filter()
        try:
            filter.run([], doc)
        except:
            self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 0)

    def test_run_method_undefined_acronym(self):
        doc = self._loadJSONDocument("sample-text.md")
        acronyms = return_local_test_data("two_basic_acronyms.json")
        filter = Filter()
        try:
            filter.run([acronyms], doc)
        except:
            self.fail("calling the run method should not fail")
        self.assertEqual(filter.index.occurences('bba'), 2)
        self.assertEqual(filter.index.occurences('undef'), 0)

    def _createAcronymsDictionary(self, filename):
        with open(return_local_test_data(filename), "r") as handle:
            return Acronyms.Read(handle)

    def _loadJSONDocument(self, filename):
        data = convert_to_json(return_local_test_data(filename))
        doc = panflute.load(io.StringIO(data))
        return doc


if __name__ == '__main__':
    unittest.main()
