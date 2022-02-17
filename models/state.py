#!/usr/bin/python3
"""
State Module
Inherits from BaseModel
Has attributes for States
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State
    name (string): State Name
    """
    name = ''
