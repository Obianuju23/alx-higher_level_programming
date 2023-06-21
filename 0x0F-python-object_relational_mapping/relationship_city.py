#!/usr/bin/python3

""" class that defines Cities and inherits Base instance from the model_state
which is an instance of the declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Definition of the City class
    Inherits an instance of Base from the State class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
