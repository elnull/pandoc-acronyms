# The Click application that is the front-end to the acronyms filter.

import sys
import os
import click
from acronyms.acronym_filter import Filter
from acronyms.logging import configure_logging, error, debug


@click.command()
@click.option('-a', '--acronyms', envvar='ACRONYMS', default="", help='A file with acronym definitions in JSON format.', multiple=True)
@click.option('-v', '--verbose/--no-verbose', default=False, help='Enable verbose (debug) output.')
@click.argument('format', nargs=-1)
def filter(acronyms, verbose, format):
    """The pandoc-acronyms filter."""
    filter = Filter()
    configure_logging(verbose)
    debug("command line: {}".format(" ".join(sys.argv)))
    try:
        filter.run(acronyms)
    except Exception as e:
        error(str(e))
        if verbose:
            raise e


if __name__ == '__main__':
    filter()  # pylint: disable=no-value-for-parameter
