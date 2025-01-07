from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.core.sock import Sock
from typing import Tuple
from app.clients.db import DatabaseClient


def create_sock_router(database_client: DatabaseClient) -> APIRouter:
    sock_router = APIRouter()

    @sock_router.get("/heel-start-length/")
    async def get_heel_start_length(
        row_gauge: int | float,
        foot_length: int | float,
        size: str,
        yarn_weight: str,
    ) -> float:
        sock = Sock(database_client=database_client, size=size, yarn_weight=yarn_weight)
        side_heel_section, _, _ = sock.heel_stitch_sections
        no_heel_rows = side_heel_section * 2
        heel_length = no_heel_rows / row_gauge
        heel_start_length = foot_length - heel_length
        return heel_start_length

    @sock_router.get("/heel-stitch-sections/")
    async def get_heel_stitch_sections(
        size: str, yarn_weight: str
    ) -> Tuple[int, int, int]:
        """
        Construct the heel layout.
        """
        sock = Sock(database_client=database_client, size=size, yarn_weight=yarn_weight)
        return sock.heel_stitch_sections

    @sock_router.get("/full-pattern/")
    async def get_full_pattern(size: str, yarn_weight: str) -> PlainTextResponse:
        """
        Get full pattern for sock pattern
        """
        sock = Sock(database_client=database_client, size=size, yarn_weight=yarn_weight)
        return sock.full_pattern

    return sock_router
