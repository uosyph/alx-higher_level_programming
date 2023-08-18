#!/usr/bin/python3
"""Contains the class definition of a State and an instance of Base"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)

    def __str__(self):
        """Class str"""
        return f"{self.id}: {self.name}"
