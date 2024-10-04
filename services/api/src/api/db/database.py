# Third party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db:5432/monitoring"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"sslmode": "disable"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    """
    Get the database session
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
