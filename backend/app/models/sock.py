from sqlalchemy import String, Float, Column, Enum, Integer, UniqueConstraint
from .base import Base


class ShoeSize(Base):
    """
    Table for  shoe sizes

    :eu: EU shoe size - primary key
    :us: US shoe size
    :uk: UK shoe size
    :foot_length_cm: Foot length in cm
    :knit_size: Mapping of shoe size to sock size for knitting, one of B (baby), T (toddler), C (child), S (small adult), M (medium adult), L (large adult), XL (extra-large adult)
    """

    # knit siz eiwll be foreign key to a primary key in the stitch count table
    __tablename__ = "shoesize"
    eu = Column(Integer, primary_key=True, index=True, nullable=False)
    us = Column(Integer, nullable=False)
    uk = Column(Integer, nullable=False)
    foot_length_cm = Column(Float, nullable=False)
    knit_size = Column(Enum("B", "T", "C", "S", "M", "L", "XL", name="knit_size"))


class StitchCount(Base):
    """
    Reference table for stitch count per knit_size (maps to shoesize table)
    :knit_size: Size of sock, one of B (baby), T (toddler), C (child), S (small adult), M (medium adult), L (large adult), XL (extra-large adult)
    :stitch_count: Number of stitches in middle part of sock
    """

    __tablename__ = "stitchcount"
    __table_args__ = (UniqueConstraint("knit_size", name="unique_knit_size"),)

    knit_size = Column(
        Enum("B", "T", "C", "S", "M", "L", "XL", name="knit_size"),
        primary_key=True,
        nullable=False,
    )
    yarn_weight = Column(
        Enum("Fingering", "DK", "Worsted", name="yarn_weight"), nullable=False
    )
    stitch_count = Column(Integer, nullable=False)

class Patterns(Base):
    """
    Patterns for each foot section. 
    :pattern_part: One of 'toe','middle','heel' and 'cuff'
    :pattern: String of text for the pattern with curly braces containing the variables to be filled in from the API. e.g. {stitch_count} will be updated according to the user inputs.

    """
    
    __tablename__ = "patterns"

    pattern_part = Column(        
        Enum("toe", "middle", "heel", "cuff", name="pattern_part"),
        primary_key=True,
        nullable=False,)
    
    pattern = Column(String, nullable=False)


