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

class Data(Base):
    __tablename__ = 'data'   
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    favorite_id  = Column(Integer, ForeignKey('favorite.id'))

class Favorite(Base):
    __tablename__ = 'favorite'   
    user_id= Column(Integer, primary_key=True)
    name =  Column(String(50), nullable=False, unique=True)
    data_id = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=False, unique=True)
    user_id  = Column(Integer, ForeignKey('user.id'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name_character = Column(String(50), nullable=False, unique=True)
    gender = Column(String(10))
    height = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    data_id  = Column(Integer, ForeignKey('data.id'))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planets = Column(String(50), nullable=False, unique=True)
    climate = Column(String(50))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    data_id  = Column(Integer, ForeignKey('data.id'))

class Films(Base):
    __tablename__ = 'films'
    id =  Column(Integer, primary_key=True)
    title = Column(String(50))
    episode_id = Column(String(50))
    director = Column(String(50))
    producer = Column(String(50))
    release_date = Column(Integer)
    data_id  = Column(Integer, ForeignKey('data.id'))



   

def to_dict(self):
    return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
