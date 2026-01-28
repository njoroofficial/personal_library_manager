from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# database file
DATABASE_URL = "sqlite:///library.db"

# Engine i.e the bridge to the DB

engine = create_engine(DATABASE_URL, echo=False)

# Session to use to manage data)
Session = sessionmaker(bind=engine)
session = Session()

# Base 
Base = declarative_base()