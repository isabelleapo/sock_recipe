from sqlalchemy import Float, Column, Enum, Integer, String
from base import Base
import enum

class ShoeSize(Base):
    """
    Table for  shoe sizes

    :eu: EU shoe size - primary key
    :us: US shoe size
    :uk: UK shoe size
    :foot_length_cm: Foot length in cm
    :knit_size: Mapping of shoe size to sock size for knitting, one of B (baby), T (toddler), C (child), S (small adult), M (medium adult), L (large adult), XL (extra-large adult)
    """
    __tablename__="shoesize"
    eu = Column(Integer, primary_key=True, index=True, nullable=False)
    us = Column(Integer, nullable=False)
    uk = Column(Integer, nullable=False)
    foot_length_cm = Column(Float, nullable=False)
    knit_size = Column(Enum('B', 'T', 'C', 'S', 'M', 'L', 'XL',  name='knit_size'))
    
