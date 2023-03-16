#!/usr/bin/python3
"""Contains the class definition of a State and an
instance Base = declarative_base()"""
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, CHAR


Base = declarative_base()


class State(Base):
    """
    Defines State class inherits from Base
    id (int): state id
    name (strin): state name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(128), nullable=False)
