from fastapi import FastAPI
from .routes.sock import create_sock_router
from app.clients.db import DatabaseClient
# from app.config import Config
from app.services.sock_service import SockService

sockservice = None


def create_application() -> FastAPI:
    global sockservice
    # config = Config()
    tables = ["shoesize", "stitchcount"]
    database_client = DatabaseClient(tables)

    sock_router = create_sock_router(database_client)
    app = FastAPI()
    app.include_router(sock_router)
    return app


app = create_application()