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
    favorites_character = relationship('Favorites_Character')
    favorites_planets = relationship('Favorites_Planets')
    favorites_films = relationship('Favorites_Films')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name_character = Column(String(50), nullable=False, unique=True)
    gender = Column(String(10))
    height = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    favorites_character = relationship('Favorites_Character')
       
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planets = Column(String(50), nullable=False, unique=True)
    climate = Column(String(50))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    favorites_planets = relationship('Favorites_Planets')

class Films(Base):
    __tablename__ = 'films'
    id =  Column(Integer, primary_key=True)
    title = Column(String(50))
    episode_id = Column(String(50))
    director = Column(String(50))
    producer = Column(String(50))
    release_date = Column(Integer)
    favorites_films = relationship('Favorites_Films')

class Favorites_Character(Base):
    __tablename__ = 'favorites_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Favorites_Planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class Favorites_Films(Base):
    __tablename__ = 'favorites_films'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    films_id = Column(Integer, ForeignKey('films.id'))
   

def to_dict(self):
    return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
