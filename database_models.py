
from sqlalchemy import Column , Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class product(Base):

    __tablename__ = "Product"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(500))
    price = Column(Float)
    quantity = Column(Integer)