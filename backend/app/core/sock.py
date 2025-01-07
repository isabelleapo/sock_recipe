from typing import List, Tuple
import numpy as np
from app.services.sock_service import SockService

# everything calculated in cm - european shoe sizes are unisex
class Sock:
    def __init__(self, database_client, size, yarn_weight) -> None:
        self.sock_service = SockService(database_client=database_client)
        self.size = size
        self.yarn_weight = yarn_weight
        self.stitch_count = None
        self.heel_stitch_sections = None
        self.possible_cuffs = None
        self.full_pattern = None

    async def initialize(self):
        """
        Asynchronously initialize all pattern components.
        """
        self.stitch_count = await self.get_stitch_count()
        self.heel_stitch_sections = self.get_heel_stitch_section_layout()
        self.possible_cuffs = self.get_possible_cuffs()
        self.full_pattern = await self.get_pattern()  # Since get_pattern calls async methods


    async def get_stitch_count(self) -> int:
        """
        A function that call the shoe size database and yarn weight database to return a number of stitches.
        e.g. Shoe size 37 = women's medium + fingering weight yarn = 56 stitch count
        """
        stitch_count = await self.sock_service.get_stitch_count_from_db(
            self.size, self.yarn_weight
        )
        return stitch_count

    def get_heel_stitch_section_layout(self) -> Tuple[int, int, int]:
        """
        Construct the heel layout.
        """
        print(self.stitch_count)
        equal_stitches = self.stitch_count // 3
        if self.stitch_count % 3 == 2:
            middle_stitch_count = int(np.floor(equal_stitches))
            side_stitch_count = int(np.ceil(equal_stitches))
            return (side_stitch_count, middle_stitch_count, side_stitch_count)
        if self.stitch_count % 3 == 1:
            middle_stitch_count = int(np.ceil(equal_stitches))
            side_stitch_count = int(np.floor(equal_stitches))
            return (side_stitch_count, middle_stitch_count, side_stitch_count)
        return (equal_stitches, equal_stitches, equal_stitches)

    def get_possible_cuffs(self) -> List[str]:
        cuff_rib_patterns = ["1x1"]
        if self.stitch_count % 6 == 0:
            cuff_rib_patterns.append("3x3")
        if self.stitch_count % 8 == 0:
            cuff_rib_patterns.extend(["4x4", "2x2"])
        elif self.stitch_count % 4 == 0:
            cuff_rib_patterns.append("2x2")
        return cuff_rib_patterns

    async def get_and_format_pattern_part(self, pattern_part: str) -> str:
        pattern = await self.sock_service.get_pattern_part_from_db(pattern_part)
        formatted_pattern_part = pattern.format(**vars(self))
        return formatted_pattern_part

    def get_pattern(self) -> str:
        toe = self.get_and_format_pattern_part(pattern_part="toe")
        middle = self.get_and_format_pattern_part(pattern_part="middle")
        heel = self.get_and_format_pattern_part(pattern_part="heel")

        full_pattern_string = toe + middle + heel

        return full_pattern_string
