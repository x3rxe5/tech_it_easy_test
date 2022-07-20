from fastapi import FastAPI,Depends
from sqlalchemy import join
from .schemas import CreateBillRequest,CreateChalanRequest,CreateVehicleRequest,CreateBranchRequest,FilterFieldsRequest
from sqlalchemy.orm import Session
from .database import get_db
from .models import Bilty_master,Branch_master,Vehicle_master,Chalan_master
import datetime


app = FastAPI()

@app.post("/bill")
def create_bill(details:CreateBillRequest,db:Session = Depends(get_db)):
    try:
        to_create = Bilty_master(
            bilty_no=details.bilty_no,
            bill_type=details.bill_type,
            amt=details.amt,
            chalan_id=details.chalan_id
        )

        db.add(to_create)
        db.commit()
        return {
            "success":True,
            "created_id":to_create.bilty_id
        }

    except Exception as err:
        return {
            "failure":True,
            "error":err
        }


@app.get('/bill')
def fetch_bill(db:Session = Depends(get_db)):
    try:
        return db.query(Bilty_master).all()
    except Exception as err:
        return {
            "failure":True,
            "error":err
        }


@app.post("/chalan")
def create_chalan(details:CreateChalanRequest,db:Session = Depends(get_db)):
    try:
        to_create = Chalan_master(
            chalan_no = details.chalan_no,
            chalan_date = details.chalan_date,
            inwarded = details.inwarded,
            station_from = details.station_from,
            station_to = details.station_to,
            created_from = details.created_from,
            vehicle_id = details.vehicle_id
        )

        db.add(to_create)
        db.commit()

        return {
            "success":True,
            "created_id":to_create.chalan_id
        }
    except Exception as err:
        return {
            "failure":True,
            "error":err
        }


@app.get('/chalan')
def fetch_bill(db:Session = Depends(get_db)):
    try:
        return db.query(Chalan_master).all()
    except Exception as err:
        return {
            "failure":True,
            "error":err
        }




@app.post("/branch")
def create_branch(details:CreateBranchRequest,db:Session = Depends(get_db)):
    try:
        to_create = Branch_master(
            branch_name = details.branch_name
        )
        db.add(to_create)
        db.commit()
        return {
            "success":True,
            "created_id":to_create.branch_id
        }
    except Exception as err:
        return {
            "failure":True,
            "error":err
        }


@app.get('/branch')
def fetch_bill(db:Session = Depends(get_db)):
    try:
        return db.query(Branch_master).all()
    except Exception as err:
        return {
            "failure":True,
            "error":err
        }




@app.post("/vehicle")
def create_vehicle(details:CreateVehicleRequest,db:Session = Depends(get_db)):
    try:
        to_create = Vehicle_master(
            vehicle_no = details.vehicle_no,
            owner_name = details.owner_name
        )
        db.add(to_create)
        db.commit()
        return {
            "success":True,
            "created_id":to_create.vehicle_id
        }
    except Exception as err:
        return {
            "failure":True,
            "error":err
        }


@app.get('/vehicle')
def fetch_bill(db:Session = Depends(get_db)):
    try:
        return db.query(Vehicle_master).all()
    except Exception as err:
        return {
            "failure":True,
            "error":err
        }



@app.post("/fetch")
def get_all_sorted_data(sort:str,id:int,details:FilterFieldsRequest,db:Session = Depends(get_db)):
    # try:
        return db.query(Chalan_master).filter(
            Chalan_master.created_from == details.created_from,
            Chalan_master.chalan_date.between(details.date_from,details.date_to),            
        ).join(Vehicle_master,Vehicle_master.vehicle_no == details.vehicle_no).all()
    # except Exception as err:
    #     return {
    #         "failure":True,
    #         "error":err
    #     }

