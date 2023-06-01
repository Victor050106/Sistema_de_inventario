from sqlalchemy import Column,Integer, String

from config.database import Base


class Supplier(Base):
    """create Supplier Model"""

    __tablename__ = "supplier"

    id = Column(Integer,primary_key = True)
    Name = Column(String)
    Address = Column(String)
    Phone = Column(Integer)
    Email = Column(String)
