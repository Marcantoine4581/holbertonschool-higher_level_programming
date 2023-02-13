
"""Defines a base model class."""


class Base:
    """Represent the base model.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        __nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
