#!/usr/bin/python3
"""
Review models
"""
from models.base_model import BaseModel

class review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        