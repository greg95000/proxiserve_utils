from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from db_management.base import Base

class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(Integer, primary_key=True)
    consumption = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="consumptions")