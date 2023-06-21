#!/usr/bin/python3
"""A class that defines State and Base which is an instance of
the declarative_base()
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Definition of the State class
    Inherits from the Base Parent class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="states",
                          cascade='save-update, merge, delete')
