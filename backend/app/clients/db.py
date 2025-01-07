from app.config import Config
from typing import Optional
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Select
from sqlalchemy.engine import Row

host = "postgresql://isabelle:QQyB2czq3!!?@localhost:5432/sock_recipe_db"

class DatabaseClient:
    def __init__(self, tables: Optional[list[str]]) -> None:
        self.tables = tables
        self.engine = create_engine(host, future=True)
        self.session = Session(bind=self.engine, future=True)
        self.metadata = MetaData()
        self._reflect_metadata()  # doesnt work if primary key missing - revisit this lesson 124
        if tables:  # doesnt trigger if tables is None or len(tables)==0
            self._set_internal_database_tabes(tables)

    def _reflect_metadata(self) -> None:
        self.metadata.reflect(bind=self.engine)  # doesnt work if primary key missing

    def _set_internal_database_tabes(self, tables: list[str]):
        for table in tables:
            setattr(self, table, self.metadata.tables[table])

    def get_first(self, query: Select) -> Optional[Row]:
        with self.session.begin():
            res = self.session.execute(query).first()
        return res

    def get_all(self, query: Select) -> list[Row]:
        with self.session.begin():
            res = self.session.execute(query).all()
        return res

    def get_paginated(self, query: Select, limit: int, offset: int) -> list[Row]:
        query = query.limit(limit).offset(offset)
        return self.get_all(query=query)
