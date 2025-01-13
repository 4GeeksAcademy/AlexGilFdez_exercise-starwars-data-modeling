import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    favorite_planets = relationship('Favorite_Planets', back_populates='user')
    favorite_characters = relationship('Favorite_Characters', back_populates='user')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(50))
    people = relationship('Characters', back_populates='planet')
    favorites_by = relationship('Favorite_Planets', back_populates='planet')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(50))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planets', back_populates='people')
    favorites_by = relationship('Favorite_Characters', back_populates='character')

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favorite_planets')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planets', back_populates='favorites_by')

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))  
    user = relationship('User', back_populates='favorite_characters')
    character_id = Column(Integer, ForeignKey('characters.id'))  
    character = relationship('Characters', back_populates='favorites_by')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
