#!/usr/bin/python3

"""
Amenity Module
inherits from basemodel
amenities in locations
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity
    name: string - empty string
    """
    name = ''
