from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


#Таблица агента
class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    city = Column(String)
    profile_photo = Column(String)
    password = Column(String)

    reg_date = Column(DateTime)



#Таблица колонок игрока
class Player_Column(Base):
    __tablename__ = 'player_columns'
    id = Column(Integer, autoincrement=True, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    column_text = Column(String)

    publish_date = Column(DateTime)
    agent_fk = relationship(Agent, lazy='subquery')


#Таблица фотографий игрока
class PlayerPhoto(Base):
    __tablename__ = 'player_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    column_id = Column(Integer, ForeignKey('player_columns.id'))
    palyer_photo = Column(String)

    column_fk = relationship(Player_Column, lazy='subquery')


#Таблица скаутских заключений
class Scout_conclusion(Base):
    __tablename__ = 'scout_conclusion'
    id = Column(Integer, autoincrement=True, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    column_id = Column(Integer, ForeignKey('player_columns.id'))
    conclusion_text = Column(String)

    agent_fk = relationship(Agent, lazy='subquery')
    column_fk = relationship(Player_Column, lazy='subquery')


#Таблица коллеги
class Colleague(Base):
    __tablename__ = 'colleagues'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    city = Column(String)

    agent_id = Column(Integer, ForeignKey('agents.id'))
    agent_fk = relationship(Agent, lazy='subquery')

    reg_date = Column(DateTime)