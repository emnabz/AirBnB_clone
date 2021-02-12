#!/usr/bin/python3
"""
Base module for Air BnB module
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    defines all common attributes and methods for other classes
    """
    def __init__(self):
    """
    creates a BaseModel object
    """
    Arguments:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now.datetime.today()
        self.updated_at = datetime.now.datetime.today()
        
    def __str__(self):
        """
        print the instance
        :return:
        """
        return ("[{}] ({}) {})".format(
            __class__.__name__,
            self.id,
            self.__dict__))

 def save(self):
        """
        update an object and save it with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dict containing all keys/values of the instance
        """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.name__
        dic['_updated_at'] = self.updated_at
        dic['created_at'] = self.created_at

        return dic
