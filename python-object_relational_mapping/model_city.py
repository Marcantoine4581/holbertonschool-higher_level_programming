#!/usr/bin/python3
"""Contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Defines City class inherits from Base
    id (int): The id of the class City
    name (string): The name of the class City
    state_id (int): The id of the state the city belong to
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
