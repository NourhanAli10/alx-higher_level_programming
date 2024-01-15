#!/usr/bin/python3
"""
State module
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan', back_populates='state')
