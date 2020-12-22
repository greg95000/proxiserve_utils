from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db_management.base import Base
from sqlalchemy.schema import Table

association_table = Table(
    'apartments_users', Base.metadata,
    Column('apartment_id', Integer, ForeignKey('apartments.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True)
    floor = Column(Integer)
    door_number = Column(Integer)
    typology = Column(String)
    area = Column(Float)
    users = relationship("User", secondary=association_table, backref="apartments")
