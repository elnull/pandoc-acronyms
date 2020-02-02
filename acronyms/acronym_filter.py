# a Pandoc filter for acronyms based on panflute.

import panflute
import sys
import re
import click

from acronyms.acronyms import Acronyms
from acronyms.index import Index
from acronyms.logging import debug, info


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
                info('Loading acronyms from {}...'.format(input))
                with open(input, "r") as handle:
                    dictionary = Acronyms.Read(handle)
                    self.acronyms.merge(dictionary)
        else:
            info('No acronym definitions specified!')
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

    # FIXME outdated
    def replace_acronym(self, matchtext, acronym, firstuse):
        text = acronym.shortform
        if firstuse:
            text = "{} ({})".format(acronym.longform, acronym.shortform)
        return text

    def process_string_token(self, token, replacer):
        rx = re.compile(r'(\[\!.+?\])')
        result = ""
        while token:
            match = rx.search(token)
            if match:
                (left, right) = match.span()
                result += token[0:left]
                pattern = token[left:right]
                result += replacer(pattern)
                token = token[right:]
            else:
                # no match left in token
                result += token
                token = ""
        return result

    def maybe_replace(self, element, match):
        # TODO There may be more than one match, e.g. "FOSS-based-GDP"
        text = match.group(1)

        acronyms = self.acronyms
        # is this an acronym?
        acronym = acronyms.get(text)
        if not acronym:
            info("Warning: acronym {} undefined.".format(text))
            return
        # register the use of the acronym:
        count = self.index.register(acronym)
        # # is this the first use of the acronym?
        if count == 1:
            info("First use of acronym {} found.".format(text))
            element.text = self.replace_acronym(element.text, acronym, True)
        else:
            debug("Acronym {} found again.".format(text))
            element.text = self.replace_acronym(element.text, acronym, False)

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
