# The Click application that is the front-end to the acronyms filter.

import click
from acronyms.acronym_filter import Filter


@click.command()
@click.option('-a', '--acronyms', default="", help='A file with acronym definitions in JSON format.', multiple=True)
@click.option('-v', '--verbose/--no-verbose', default=False, help='Enable verbose (debug) output.')
def filter(acronyms, verbose):
    """The pandoc-acronyms filter."""
    filter = Filter()
    filter.verbose = verbose

    try:
        filter.temp_run(acronyms)
    except Exception as e:
        click.secho(str(e), fg='red', err=True)
        if verbose:
            raise e


if __name__ == '__main__':
    filter()  # pylint: disable=no-value-for-parameter
