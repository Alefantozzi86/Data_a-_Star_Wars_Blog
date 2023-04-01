import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

   
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(15), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name_character = Column(String(50), nullable=False, unique=True)
    gender = Column(String(10))
    height = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
       
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planets = Column(String(50), nullable=False, unique=True)
    climate = Column(String(50))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

class Films(Base):
    __tablename__ = 'films'
    id =  Column(Integer, primary_key=True)
    title = Column(String(50))
    episode_id = Column(String(50))
    director = Column(String(50))
    producer = Column(String(50))
    release_date = Column(Integer)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable= False)
    user_id = Column(Integer)
    films_id = Column(Integer)
    character_id = Column(Integer)
    planets_id = Column(Integer)

def to_dict(self):
    return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
