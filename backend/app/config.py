from pydantic import PostgresDsn
from pydantic_settings import BaseSettings #to not have to call look for env variables each time

class Config(BaseSettings):
    host: PostgresDsn

    class Config:
        env_prefix = "db_"