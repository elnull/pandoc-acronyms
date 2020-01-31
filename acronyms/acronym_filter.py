# a Pandoc filter for acronyms based on panflute.

import panflute
import sys
import re
import click

from acronyms.acronyms import Acronyms
from acronyms.index import Index
from acronyms.logging import debug


class Filter:
    """The Filter class manages the configuration of a single filter run."""

    def __init__(self):
        self.acronyms = Acronyms()
        self.index = Index()

    @property
    def acronyms(self):
        return self._acronyms

    @acronyms.setter
    def acronyms(self, value):
        self._acronyms = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    def run(self, acronymfiles, doc=None):
        if acronymfiles:
            for input in acronymfiles:
                debug('Loading acronyms from {}...'.format(input))
                with open(input, "r") as handle:
                    dictionary = Acronyms.Read(handle)
                    self.acronyms.merge(dictionary)
        else:
            debug('No acronym definitions specified!')
        return self.process_document(doc)

    def filter_acronyms(self, element, doc):
        """The panflute filter function."""
        if type(element) == panflute.Str:
            match = self.is_match(element.text)
            if match:
                self.maybe_replace(element, match)

    def is_match(self, elementtext):
        """is_match returns True if the element is recognized as an acronym."""
        expression = Filter.match_expression()
        match = expression.match(elementtext)
        return match

    def maybe_replace(self, element, match):
        text = match.group(1)

        acronyms = self.acronyms
        # is this an acronym?
        acronym = acronyms.get(text)
        if not acronym:
            debug("Warning: acronym {} undefined.".format(text))
            return
        # register the use of the acronym:
        count = self.index.register(acronym)
        # # is this the first use of the acronym?
        if count == 1:
            debug("Debug: first use of acronym {} found.".format(text))
            element.text = "{} ({})".format(
                acronym.longform, acronym.shortform)
        else:
            debug("Debug: acronym {} found again.".format(text))
            element.text = acronym.shortform

    def process_document(self, doc):
        """The entry method to execute the filter."""
        # We need state in the filter function, so we create a filter function that references the filter object:

        def filter_closure(element, doc):
            return self.filter_acronyms(element, doc)

        return panflute.run_filter(filter_closure, doc=doc)
        # return doc.walk(filter_closure)

    @staticmethod
    def match_expression():
        return re.compile(r'\[\!(.+)\]')
