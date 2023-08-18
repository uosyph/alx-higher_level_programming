#!/usr/bin/python3
"""Contains the class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Class City"""

    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)

    def __str__(self):
        """Class str"""
        return f"{self.id}: {self.name}"
