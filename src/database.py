from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

my_secret_db = os.getenv("DATABASE_NAME")
my_secret_db_password = os.getenv("DATABASE_PASSWORD")


SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:{my_secret_db_password}@localhost/{my_secret_db}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    except Exception as err:
        print("error occured -> ",err)
        db.close()