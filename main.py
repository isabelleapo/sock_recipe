from fastapi import FastAPI
import numpy as np
from typing import Tuple

app = FastAPI

@app.get("/heel-start-length/")
async def get_heel_start_length(row_gauge: int | float, foot_length: int | float, heel_stitch_sections: Tuple[int]) -> float:
    side_heel_section, _, _ = heel_stitch_sections
    no_heel_rows = side_heel_section*2
    heel_length = no_heel_rows/row_gauge
    heel_start_length = foot_length - heel_length
    return heel_start_length

@app.get("/heel-stitch-sections/")
async def get_heel_stitch_sections(stitch_count: int)-> Tuple[int]:
    """
    Construct the heel layout.
    """
    equal_stitches = stitch_count/3
    if stitch_count%3 == 2:
        middle_stitch_count = int(np.floor(equal_stitches))
        side_stitch_count = int(np.ceil(equal_stitches))
        return (side_stitch_count, middle_stitch_count, side_stitch_count)
    if stitch_count%3 == 1:
        middle_stitch_count = int(np.ceil(equal_stitches))
        side_stitch_count = int(np.floor(equal_stitches))
        return (side_stitch_count, middle_stitch_count, side_stitch_count)
    return (equal_stitches, equal_stitches, equal_stitches)