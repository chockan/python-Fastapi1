from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# MySQL Database URL with correct host and credentials
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Yogan@localhost/fastapipractice"  # replace 'localhost' if needed

# Create engine (no need for connect_args for MySQL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is used to get a session (database connection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

def get_db():
    """
    Dependency function to get the database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
