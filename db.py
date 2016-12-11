#!/usr/bin/env python
"""
A quick script to allow us to deploy our Blog schema easily
using SQLAlchemy.

In the case of the future we need to write up any migrations for schema changes
(see https://sqlalchemy-migrate.readthedocs.io/en/latest/) this would be
the utility to add that functionality to
"""
import click

from sqlalchemy import create_engine
from blog.model.store import PostMeta

engine = None


@click.group()
@click.option('--uri', help="SQLAlchemy URI to deploy schema to")
def cli(uri):
    click.echo('Using "%s" connection URI'.format(uri))
    PostMeta.create_all(engine)

@cli.command()
def deploy():
    PostMeta.create_all(engine)


if __name__ == '__main__':
    cli()
