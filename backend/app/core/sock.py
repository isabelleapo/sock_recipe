from typing import List, Tuple
import numpy as np
from services import SockService

sock_service = SockService


# everything calculated in cm - european shoe sizes are unisex
class Sock:
    def __init__(self, size, yarn_weight) -> None:
        self.size = size
        self.yarn_weight = yarn_weight
        self.stitch_count = self.get_stitch_count()
        self.heel_stitch_sections = self.get_heel_stitch_section_layout()
        self.possible_cuffs = self.get_possible_cuffs()
        self.full_pattern = self.get_pattern()

    def get_stitch_count(self) -> int:
        """
        A function that call the shoe size database and yarn weight database to return a number of stitches.
        e.g. Shoe size 37 = women's medium + fingering weight yarn = 56 stitch count
        """
        stitch_count = sock_service.get_stitch_count_from_db(
            self.size, self.yarn_weight
        )
        return stitch_count

    def get_heel_stitch_section_layout(self) -> Tuple[int]:
        """
        Construct the heel layout.
        """
        equal_stitches = self.stitch_count / 3
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

    def get_and_format_pattern_part(self, pattern_part: str) -> str:
        pattern = sock_service.get_pattern_part_from_db(pattern_part)
        formatted_pattern_part = pattern.format(**vars(self))
        return formatted_pattern_part

    def get_pattern(self) -> str:
        toe = self.get_and_format_pattern_part(pattern_part="toe")
        middle = self.get_and_format_pattern_part(pattern_part="middle")
        heel = self.get_and_format_pattern_part(pattern_part="heel")

        full_pattern_string = toe + middle + heel

        return full_pattern_string


sock1 = Sock(size="37", yarn_weight="fingering")
# print(sock1.full_pattern)
