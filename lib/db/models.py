from sqlalchemy import (PrimaryKeyConstraint, create_engine, Column, Integer, String, DECIMAL)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class WarDrobe(Base):
    
    __tablename__ = 'wardrobes'
    
    __table_args__ = (PrimaryKeyConstraint('id'), )
    
    id = Column(Integer())
    name = Column(String())
    price = Column(String())
    
    Column
    
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        
    def __repr__(self):
        return "<Wardrobe(id='%s', name='%s', price='%s')>" % (self.id, self.name, self.price)
    
engine = create_engine('sqlite:///example.db', echo=True)
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind=engine)
session = Session()

#---create a wardrobe---
# wardrobe = WarDrobe(1, 'Wardrobe', 1000)
# session.add(wardrobe)
# session.commit()

#---create multiple wardrobes---
# w1 = WarDrobe(1, 'Wardrobe', 1000)
# w2 = WarDrobe(2, 'Wardrobe', 1000)
# w3 = WarDrobe(3, 'Wardrobe', 1000)

#---add multiple wardrobes---
# session.add_all([w1, w2, w3])

#---update a wardrobe---
# results = session.query(WarDrobe).all()
# print(results)