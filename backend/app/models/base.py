from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgres://isabelle:QQyB2czq3!!?@localhost:5432/sock_recipe_db"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()