from sqlalchemy import Column, Integer, String
from config.database import Base


class Product(Base):
    """create Product Model"""
    
    __tablename__ = "product"
    
    id = Column(Integer, primary_key = True)
    name =  Column(String)
    brand = Column(String)
    description = Column(String)
    price = Column(float)
    entry_date = Column(Integer)