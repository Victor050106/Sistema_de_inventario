from sqlalchemy import Column, Integer, String
from config.database import Base


class Product(Base):
    """create Product Model"""
    
    __tablename__ = "product"
    
    id = Column(Integer, primary_key = True)
    Name =  Column(String)
    Brand = Column(String)
    Description = Column(String)
    Price = Column(float)
    Entry_Date = Column(Integer)