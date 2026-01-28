from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base, session

class Book(Base):
    __tablename__ = 'books'

    # Columns
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    
    # Foreign Key: Links this book to a specific author ID
    author_id = Column(Integer, ForeignKey('authors.id'))

    # Relationship: Allows us to access the full Author object
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}')>"


    @classmethod
    def create(cls, title, year, author_id):
        new_book = cls(title=title, year=year, author_id=author_id)
        session.add(new_book)
        session.commit()
        return new_book

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, book_id):
        return session.query(cls).filter_by(id=book_id).first()

    def delete(self):
        session.delete(self)
        session.commit()