from .cfg_db import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .tables import Chetv, DomZad, DomZadEmpty, Poned, Pyant, Sred, Vtorn
from datetime import datetime
from .predmets import weekday_day, weekday_dz, days

conn = create_engine(URL(**DATABASE))

DeclarativeBase = declarative_base()

DeclarativeBase.metadata.create_all(conn)

Session = sessionmaker(bind=conn)
session = Session()

def new_dz(name, dz):
    session.query(DomZad).filter(DomZad.name==name).update({'dz':f'{dz}'})
    session.commit()

def new_dz_empty(dz):
    session.query(DomZadEmpty).filter(DomZadEmpty.name=='first').update({'dz':f'{dz}'})
    session.commit()

def show_new_dz():
    return session.query(DomZadEmpty).first()

def show_dz():
    return session.query(DomZad).all()

def show_dz_day_filtred(name):
    return session.query(DomZad).join(weekday_day[days[name]], DomZad.name == weekday_dz[days[name]]).all()

def show_dz_day():
    weekday = datetime.now().weekday() + 1
    if weekday in weekday_dz:
        return session.query(DomZad).join(weekday_day[weekday], DomZad.name == weekday_dz[weekday]).all()
    else:
        return 'Завтра выходной, отдыхай!'

def show_dz_filtred(name):
    return session.query(DomZad).filter(DomZad.name==name).first()