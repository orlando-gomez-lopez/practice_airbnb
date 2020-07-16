#!/usr/bin/python3
""" module point 9 review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""

    place_id = ""
    user_id = ""
    text = ""
