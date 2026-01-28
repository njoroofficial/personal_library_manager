from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.connection import Base, session

class Author(Base):
    __tablename__ = 'authors'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship
    
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

   

    @classmethod
    def create(cls, name):
        """Creates a new author and saves to DB."""
        new_author = cls(name=name)
        session.add(new_author)
        session.commit()
        return new_author

    @classmethod
    def get_all(cls):
        """Returns all authors."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, author_id):
        """Finds an author by ID."""
        return session.query(cls).filter_by(id=author_id).first()
        
    @classmethod
    def find_by_name(cls, name):
        """Finds an author by Name."""
        return session.query(cls).filter_by(name=name).first()

    def delete(self):
        """Deletes this author instance."""
        session.delete(self)
        session.commit()