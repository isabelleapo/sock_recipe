from app.clients.db import DatabaseClient
from sqlalchemy import select
# fake database

shoe_size_db = {
    "37": {"fingering": 56, "sport": 48},
    "38": {"fingering": 60, "sport": 52},
    "39": {"fingering": 64, "sport": 56},
}

pattern_parts = {
    "toe": "This is the toe pattern. Cast on {stitch_count}",
    "middle": "This is the middle pattern. No inputs.",
    "heel": "Use the calculator to find out when to start your heel. It will depend on your row gauge and stitch count. Knit across one needle. Separate the stitches on the next needle into three sections with {heel_stitch_sections[0]}, {heel_stitch_sections[1]} and {heel_stitch_sections[2]},  stitches…",
}


class SockService:
    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def get_stitch_count_from_db(self, shoe_size: str, yarn_weight: str) -> int:
        query = select(self.database_client.stitchcount).where(self.database_client.stitchcount.c.shoe_size == shoe_size).where(self.database_client.stitchcount.c.yarn_weight == yarn_weight)
        return shoe_size_db[shoe_size][yarn_weight]

    async def get_pattern_part_from_db(self, pattern_part: str) -> str:
        return pattern_parts[pattern_part]
