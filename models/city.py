#!/usr/bin/pythom3
"""
city module
"""
from models.base_model import BaseModel

class city(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
