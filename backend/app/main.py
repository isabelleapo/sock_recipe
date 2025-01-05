from fastapi import FastAPI
from .routes.sock import create_sock_router
from app.clients.db import DatabaseClient
from app.config import Config
from app.services.sock_service import SockService

sock_service = None


def create_application() -> FastAPI:
    global sock_service
    config = Config()
    tables = ["shoesize", "stitchcount"]
    database_client = DatabaseClient(config, tables)

    sock_service = SockService(database_client)

    sock_router = create_sock_router()
    app = FastAPI()
    app.include_router(sock_router)
    return app
