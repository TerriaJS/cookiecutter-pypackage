"""{{ cookiecutter.repo_name }} command line interface."""

import click


@click.command()
def cli() -> int:
    """Return zero."""
    return 0
