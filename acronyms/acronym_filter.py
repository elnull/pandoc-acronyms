# a Pandoc filter for acronyms based on panflute.

import panflute
import sys
import re

class Filter:
    """The Filter class manages the configuration of a single filter run."""
    def __init__(self):
        pass

    def filter_acronyms(self, element, doc):
        """The panflute filter function."""
        if type(element) == panflute.Str:
            if self.is_match(element.text):
                self.maybe_replace_acronym(element)
    
    def is_match(self, elementtext):
        """is_match returns True if the element is recognized as an acronym."""
        expression = Filter.match_expression()
        match = expression.match(elementtext)
        return match is not None

    def maybe_replace_acronym(self, element):
        print("[{}] {}".format(type(element).__name__, element.text), file=sys.stderr)
        # is this an acronym?
        # is this the first use of the acronym?
        pass

    @staticmethod
    def match_expression():
        return re.compile(r'(\[\!.+\])')

def run_acronyms_filter(doc):
    """The entry method to execute the filter."""
    filter = Filter()
    # We need state in the filter function, so we create a filter function that references the filter object:
    def filter_closure(element, doc):
        return filter.filter_acronyms(element, doc)
    return doc.walk(filter_closure)
