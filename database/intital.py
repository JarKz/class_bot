from .tables import DomZad, DomZadEmpty, Poned, Vtorn, Sred, Chetv, Pyant, initialise0, initialise1
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from .db import DATABASE, DeclarativeBase
from .predmets import items, pon, vtorn, sred, chetv, pyatn

# session.add_all([item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8])

def initialise():
    conn = create_engine(URL(**DATABASE))
    Session = sessionmaker(bind=conn)
    session = Session()
    initialise1()
    initialise0()
    for name in items:
        item = DomZad(name=name, dz='нету')
        session.add(item)
    for item in pon:
        session.add(item)
    for item in vtorn:
        session.add(item)
    for item in sred:
        session.add(item)
    for item in chetv:
        session.add(item)
    for item in pyatn:
        session.add(item)
    item = DomZadEmpty(name = 'first',dz = '-')
    session.add(item)
    session.commit()