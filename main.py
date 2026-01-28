import click
from lib.db.connection import Base, engine
from lib.models.author import Author
from lib.models.book import Book
from lib.cli.main_menu import start

@click.group()
def cli():
    """Manage your personal library."""
    pass

@cli.command()
def initdb():
    """Initialize the database"""
    Base.metadata.create_all(engine)
    click.echo("Database initialized successfully.")

@cli.command()
def run():
    """Start the application menu."""
    # Ensure DB exists before running
    Base.metadata.create_all(engine)
    start()

if __name__ == "__main__":
    cli()