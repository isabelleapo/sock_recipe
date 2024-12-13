from fastapi import FastAPI
import numpy as np
from typing import Tuple
from app.routes import create_sock_router


def create_application()->FastAPI:
    sock_router = create_sock_router()

    app = FastAPI()
    app.include_router(sock_router)
    return app


app = create_application()