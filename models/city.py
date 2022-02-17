#!/usr/bin/python3
"""
City Module
inherits from basemodel
cities to be assigned
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class city
    state_id: string - empty string: it will be the
    State.id
    name: string - empty string
    """
    state_id = ''
    name = ''
