from fastapi import APIRouter
from core import Sock
from typing import Tuple


def create_sock_router() -> APIRouter:
    sock_router = APIRouter()

    @sock_router.get("/heel-start-length/")
    async def get_heel_start_length(
        row_gauge: int | float,
        foot_length: int | float,
        heel_stitch_sections: Tuple[int],
    ) -> float:
        side_heel_section, _, _ = heel_stitch_sections
        no_heel_rows = side_heel_section * 2
        heel_length = no_heel_rows / row_gauge
        heel_start_length = foot_length - heel_length
        return heel_start_length

    @sock_router.get("/heel-stitch-sections/")
    async def get_heel_stitch_sections(size: int, yarn_weight: str) -> Tuple[int]:
        """
        Construct the heel layout.
        """
        sock = Sock(size=size, yarn_weight=yarn_weight)
        return sock.heel_stitch_sections

    return sock_router
