from fastapi import FastAPI
from .routes.sock import create_sock_router
def create_application()->FastAPI:
    sock_router = create_sock_router()

    app = FastAPI()
    app.include_router(sock_router)
    return app

from .models import recreate_postgres_tables
recreate_postgres_tables()
app = create_application()