from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db_management.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    mail = Column(String)
    password = Column(String)
    comsuption_last_date = Column(Date)
    consumptions = relationship("Consumption", back_populates="user")