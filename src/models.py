from xmlrpc.client import DateTime
from sqlalchemy import ForeignKey, Integer,String,Enum
from sqlalchemy.sql.schema import Column
from .database import Base
from collections import namedtuple
from sqlalchemy.orm import relationship

def create_named_tuple(*values):
     return namedtuple('NamedTuple', values)(*values)

amount_details = create_named_tuple(1,2,3)



class Bilty_master(Base):

    __tablename__ = "bilty_master"

    bilty_id = Column(Integer,primary_key=True)
    bilty_no = Column(Integer,nullable=False)
    bill_type = Column(Integer,nullable=False)
    amt = Column(Enum(*amount_details._asdict().values(), name='amount_details'))
    chalan_id = Column(Integer,ForeignKey("chalan_master.chalan_id"))


class Chalan_master(Base):

    __tablename__ = "chalan_master"

    chalan_id = Column(Integer,primary_key=True)
    chalan_no = Column(Integer,nullable=False)
    chalan_date = Column(DateTime,nullable=False)
    inwarded = Column(Integer,nullable=False)
    station_from = Column(Integer,ForeignKey("branch.branch_id"))
    station_to = Column(Integer,ForeignKey("branch.branch_id"))
    created_from = Column(Integer,nullable=False)
    vehicle_id = Column(Integer,ForeignKey("vehicle_master.vehicle_id"))

    # Relationship
    children = relationship("Bilty_master")


class Vehicle_master(Base):

    __tablename__ = "vehicle_master"

    vehicle_id = Column(Integer,primary_key=True)
    vehicle_no = Column(Integer,nullable=False)
    owner_name = Column(String,nullable=False)

    children = relationship("Chalan_master")


class Branch_master(Base):

    __tablename__ = "branch"

    branch_id = Column(Integer,primary_key=True)
    branch_name = Column(String,nullable=False)

    children = relationship("Chalan_master")