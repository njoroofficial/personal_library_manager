from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base, session
import datetime

class Book(Base):
    __tablename__ = 'books'

    # Columns
    id = Column(Integer, primary_key=True)
    _title = Column("title", String, nullable=False)
    _year = Column("year", Integer)
    
    # Foreign Key: Links this book to a specific author ID
    author_id = Column(Integer, ForeignKey('authors.id'))

    # Relationship: Allows us to access the full Author object
    author = relationship("Author", back_populates="books")

    def __init__(self, title, year, author_id):
        self.title = title
        self.year = year
        self.author_id = author_id

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}')>"
    
    # contraints methods
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Book title cannot be empty.")
        self._title = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.datetime.now().year
        if not isinstance(value, int):
             # Try to cast string to int 
            try:
                value = int(value)
            except ValueError:
                raise ValueError("Year must be a number.")
        
        if value > current_year:
             raise ValueError(f"Year cannot be in the future. (Current year: {current_year})")
        
        self._year = value


    @classmethod
    def create(cls, title, year, author_id):
        """Creates a new book and saves to DB."""
        try:
            new_book = cls(title=title, year=year, author_id=author_id)
            session.add(new_book)
            session.commit()
            return new_book
        except ValueError as e:
            print(f"Error creating book: {e}")
            return None

    @classmethod
    def get_all(cls):
        """Returns all books."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, book_id):
        """Finds a book by ID."""
        return session.query(cls).filter_by(id=book_id).first()

    def delete(self):
        """Deletes this book instance."""
        session.delete(self)
        session.commit()