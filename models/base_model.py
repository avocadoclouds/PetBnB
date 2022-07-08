#!/usr/bin/python3
"""Module with a class"""
import uuid
import datetime


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes.
    """
    # self stands for the instance itself

    def __init__(self, id, created_at, updated_at):
        """
        Defines public instance attributes:
            id: (string) That's assigned a unique id.
            created_at: (datetime) That's assigned the current date
                        when an instance is created.
            updated_at: (datetime) That's assigned the the current datetime
                        when an instance is created and it will be updated
                        every time you change your object.
        """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

        id = uuid.uuid4()

        # .now() picks up the current time when instance is intialised
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns the class name and id of an instance"""

        # for the name of class use -> self.__class__.__name__
        """self.__dict__ is a dictionary that stores
            an instances's writable attributes"""

        info = print("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))
        return info
