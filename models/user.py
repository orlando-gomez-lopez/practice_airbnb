#!/usr/bin/python3
""" module point 8 user class """
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
