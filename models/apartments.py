from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db_management.base import Base

class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True)
    floor = Column(Integer)
    door_number = Column(Integer)
    typology = Column(String)
    area = Column(Float)

