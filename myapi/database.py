from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = "sqlite:///./myapi.db"

engin = create_engine(
    SQLALCHAMY_DATABASE_URL, connect_args={"cheeck_same_thread": False}
)
sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()