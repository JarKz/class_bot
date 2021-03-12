from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from .db import DATABASE
from sqlalchemy.engine.url import URL

conn = create_engine(URL(**DATABASE))
DeclarativeBase = declarative_base()

class DomZad(DeclarativeBase):
    __tablename__ = 'domzad'

    id = Column(Integer, primary_key=True)
    name = Column('Предмет', String)
    dz = Column('Д/з', String)

    def __repr__(self) -> str:
        return '%s -- %s' % (self.name, self.dz)

class DomZadEmpty(DeclarativeBase):
    __tablename__ = 'empty_dz'

    id = Column(Integer, primary_key=True)
    name = Column('Пустота', String)
    dz = Column('Д/з', String)

    def __repr__(self) -> str:
        return '%s' % (self.dz)

class Poned(DeclarativeBase):
    __tablename__ = 'poned'

    id = Column(Integer, primary_key=True)
    name = Column('Предмет', String)

class Vtorn(DeclarativeBase):
    __tablename__ = 'vtorn'

    id = Column(Integer, primary_key=True)
    name = Column('Предмет', String)

class Sred(DeclarativeBase):
    __tablename__ = 'sred'

    id = Column(Integer, primary_key=True)
    name = Column('Предмет', String)

class Chetv(DeclarativeBase):
    __tablename__ = 'chetv'

    id = Column(Integer, primary_key=True)
    name = Column('Предмет', String)

class Pyant(DeclarativeBase):
    __tablename__ = 'pyatn'

    id = Column(Integer, primary_key=True)
    name = Column('Предмет', String)

class Ovyavlenia(DeclarativeBase):
    __tablename__ = 'obyavl'

    number = Column(Integer, primary_key=True)
    name = Column('Объявление', String)

def initialise0():
    DeclarativeBase.metadata.create_all(conn)

def initialise1():
    DeclarativeBase.metadata.drop_all(conn)