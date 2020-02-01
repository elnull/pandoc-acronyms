# The API for diagnostics and debug output.
import click

_Verbose = False


def configure_logging(verbose):
    global _Verbose
    _Verbose = verbose


def debug(msg):
    if _Verbose:
        click.secho(msg, fg='yellow', err=True)


def error(msg):
    click.secho(msg, fg='red', err=True)


def fatal(msg):
    raise RuntimeError(msg)
