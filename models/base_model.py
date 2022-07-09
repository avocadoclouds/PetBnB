#!/usr/bin/python3
"""Module with a class"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes.
    """
    # self stands for the instance itself

    # def __init__(self, id, created_at, updated_at):
    #     """
    #     Defines public instance attributes:
    #         id: (string) That's assigned a unique id.
    #         created_at: (datetime) That's assigned the current date
    #                     when an instance is created.
    #         updated_at: (datetime) That's assigned the the current datetime
    #                     when an instance is created and it will be updated
    #                     every time you change your object.
    #     """
    #     self.id = id
    #     self.created_at = created_at
    #     self.updated_at = updated_at

    #     id = uuid.uuid4()

    #     # .now() picks up the current time when instance is intialised
    #     created_at = datetime.datetime.now()
    #     updated_at = datetime.datetime.now()

    id = uuid.uuid4()

    # .now() picks up the current time when instance is intialised
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """Returns the information about an instance/object like:
            Class name,
            Instance id,
            Dictionary of the attributes of instance
        """

        # for the name of class use -> self.__class__.__name__
        """self.__dict__ is a dictionary that stores
            an instances's writable attributes"""

        info = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return info

    # Pubic instance methods:

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime when changes are done.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance. Plus the class name, created_at and updated_at
        as string object in ISO format.
        """

        dic = {}
        # we need everything of __dic__ in dic, so we just assign it to dic
        dic = self.__dict__

        # then we add the rest info
        # note: keys have to be strings
        dic['__class__'] = self.__class__.__name__

        # add id after changing to str
        id = str(self.id)
        dic['id'] = id

        # change created_at & updated_at to ISO format

        created_at = str(self.created_at.isoformat())
        updated_at = str(self.updated_at.isoformat())

        # add them to dic plus the id
        dic['created_at'] = created_at
        dic['updated_at'] = updated_at

        return dic
