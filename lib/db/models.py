from sqlalchemy import (create_engine, Column, Integer, String)
from  sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class WarDrobe(Base):
    
    __tablename__ = 'wardrobe'
    
    __table_args__ = (PrimaryKeyConstraint('id'), )
    
    id = Column(Integer())
    name = Column(String())
    power = Column(String())
    
    Column