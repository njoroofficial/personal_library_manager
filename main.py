from lib.db.connection import Base, engine
from lib.models.author import Author
from lib.models.book import Book

def init_db():
    # creates tables if they don't exist
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()