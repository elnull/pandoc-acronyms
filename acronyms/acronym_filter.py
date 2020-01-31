# a Pandoc filter for acronyms based on panflute.

import panflute
import sys
import re
import click

from acronyms.acronyms import Acronyms
from acronyms.index import Index


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

    @property
    def verbose(self):
        return self._verbose

    @verbose.setter
    def verbose(self, onOff):
        self._verbose = onOff

    def debug(self, msg):
        if self.verbose:
            click.secho(msg, fg='yellow', err=True)

    # FIXME placeholder
    # FIXME implement test (doc must be passed)
    def temp_run(self, acronymfiles):
        if acronymfiles:
            for input in acronymfiles:
                self.debug('Loading acronyms from {}...'.format(input))
                with open(input, "r") as handle:
                    dictionary = Acronyms.Read(handle)
                    self.acronyms.merge(dictionary)
        else:
            self.debug('No acronym definitions specified!')

        def filter_closure(element, doc):
            return self.filter_acronyms(element, doc)

        return panflute.run_filter(filter_closure)

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
            print("Warning: acronym {} undefined.".format(
                text), file=sys.stderr)
            return
        # register the use of the acronym:
        count = self.index.register(acronym)
        # # is this the first use of the acronym?
        if count == 1:
            print("Debug: first use of acronym {} found.".format(
                text), file=sys.stderr)
            element.text = "{} ({})".format(
                acronym.longform, acronym.shortform)
        else:
            print("Debug: acronym {} found again.".format(
                text), file=sys.stderr)
            element.text = acronym.shortform

    def run(self, doc):
        """The entry method to execute the filter."""
        # We need state in the filter function, so we create a filter function that references the filter object:

        def filter_closure(element, doc):
            return self.filter_acronyms(element, doc)

        return doc.walk(filter_closure)

    @staticmethod
    def match_expression():
        return re.compile(r'\[\!(.+)\]')
