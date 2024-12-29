
from .database import Base  # Assuming Base is imported from your database module
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column

class DbUser(Base):
    __tablename__ = 'users'

    # Define the columns with reasonable string lengths
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50),)  # Added max length and index
    email = Column(String(100), unique=True, index=True)    # Added max length and index
    password = Column(String(255))  # Make sure to hash passwords before saving
    items = relationship('DbArticle', back_populates='user')


class DbArticle(Base): 
    __tablename__= 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, index=True)  # Unique constraint on title
    content = Column(String(100), index=True)  # No need to make content unique
    published = Column(Boolean, default=False)  # Default value for published
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to the 'users' table

    # Defining the relationship
    user = relationship("DbUser", back_populates="articles")