from email.policy import default
from xmlrpc.client import DateTime
from sqlalchemy import ForeignKey, Integer,String,Enum, false
from sqlalchemy.sql.schema import Column
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TSTZRANGE




class Bilty_master(Base):

    __tablename__ = "bilty_master"

    bilty_id = Column(Integer,primary_key=True)
    bilty_no = Column(Integer,nullable=False)
    bill_type = Column(Integer,nullable=False)
    amt = Column(Integer,nullable=False,default=1)
    chalan_id = Column(Integer,ForeignKey("chalan_master.chalan_id"))

    Bills = relationship("Chalan_master",back_populates="Chalan_Bill")


class Chalan_master(Base):

    __tablename__ = "chalan_master"

    chalan_id = Column(Integer,primary_key=True)
    chalan_no = Column(Integer,nullable=False)
    chalan_date = Column(TSTZRANGE(),nullable=False)
    inwarded = Column(Integer,nullable=False)
    station_from = Column(Integer,ForeignKey("branch.branch_id"))
    station_to = Column(Integer,ForeignKey("branch.branch_id"))
    created_from = Column(Integer,nullable=False)
    vehicle_id = Column(Integer,ForeignKey("vehicle_master.vehicle_id"))

    # Relationship
    Chalan_Bill = relationship("Bilty_master",back_populates="Bills")

    Chalan_station_to = relationship("Branch_master", foreign_keys=[station_from])
    Chalan_station_to = relationship("Branch_master", foreign_keys=[station_to])

    # Chalan_vehicle = relationship("Vehicle_master",foreign_keys=[vehicle_id])
    

class Vehicle_master(Base):

    __tablename__ = "vehicle_master"

    vehicle_id = Column(Integer,primary_key=True)
    vehicle_no = Column(Integer,nullable=False)
    owner_name = Column(String,nullable=False)

    # Vehicle = relationship("Chalan_master",back_populates="Chalan_Vehicle")


class Branch_master(Base):

    __tablename__ = "branch"

    branch_id = Column(Integer,primary_key=True)
    branch_name = Column(String,nullable=False)

    # Branch = relationship("Chalan_master",back_populates="Chalan_Branch")