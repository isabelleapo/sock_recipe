from sqlalchemy import Float, Column, Enum, Integer, UniqueConstraint
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
    #knit siz eiwll be foreign key to a primary key in the stitch count table
    __tablename__="shoesize"
    eu = Column(Integer, primary_key=True, index=True, nullable=False)
    us = Column(Integer, nullable=False)
    uk = Column(Integer, nullable=False)
    foot_length_cm = Column(Float, nullable=False)
    knit_size = Column(Enum('B', 'T', 'C', 'S', 'M', 'L', 'XL',  name='knit_size'))


class StitchCount(Base):
    """
    """
    __tablename__="stitchcount"
    __tableargs__= (UniqueConstraint('knit_size', name='unique_knit_size'),)

    knit_size = Column(Enum('B', 'T', 'C', 'S', 'M', 'L', 'XL',  name='knit_size'), primary_key=True, nullable=False)
    yarn_weight = Column(Enum('Fingering', 'DK', 'Worsted', name='yarn_weight'), nullable=False)
    stitch_count = Column(Integer, nullable=False)



