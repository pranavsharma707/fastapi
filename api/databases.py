

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHAMY_DATABASE_URL = "mysql+mysqlconnector://root:pranav@localhost:3306/fastapi"

engine = create_engine(SQLALCHAMY_DATABASE_URL)
Base=declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()