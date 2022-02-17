#!/usr/bin/python3
"""
module that contains subclass User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    users email, password, first and last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
