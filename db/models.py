from sqlalchemy import Column, Integer, String
from .database import Base  # Assuming Base is imported from your database module


class DbUser(Base):
    __tablename__ = 'users'

    # Define the columns with reasonable string lengths
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Added max length and index
    email = Column(String(100), unique=True, index=True)    # Added max length and index
    password = Column(String(255))  # Make sure to hash passwords before saving
