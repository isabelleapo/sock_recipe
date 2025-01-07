from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import Config

URL_DATABASE =

# config = Config()
# engine = create_engine(config.host, echo=True)
engine = create_engine(URL_DATABASE, echo=True)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine, future=True)

Base = declarative_base()


def recreate_postgres_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
