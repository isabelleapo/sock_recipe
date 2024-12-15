from fastapi import FastAPI
from app.routes.sock import create_sock_router
def create_application()->FastAPI:
    sock_router = create_sock_router()

    app = FastAPI()
    app.include_router(sock_router)
    return app

print('hi')
app = create_application()