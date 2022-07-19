from turtle import title
from fastapi import FastAPI,Depends
from .schemas import CreateBillRequest,CreateChalanRequest,CreateVehicleRequest,CreateBranchRequest,FilterFieldsRequest
from sqlalchemy.orm import Session
from .database import get_db
from .models import Bilty_master,Branch_master,Vehicle_master,Chalan_master

app = FastAPI()

@app.post("/bill")
def create_bill(details:CreateBillRequest,db:Session = Depends(get_db)):

    to_create = Bilty_master(
        bilty_no=details.bilty_no,
        bil_type=details.bil_type,
        amt=details.amt,
        chalan_id=details.chalan_id
    )

    db.add(to_create)
    db.commit()
    return {
        "success":True,
        "created_id":to_create.id
    }


@app.post("/chalan")
def create_chalan(details:CreateChalanRequest,db:Session = Depends(get_db)):

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
        "created_id":to_create.id
    }


@app.post("/branch")
def create_branch(details:CreateBranchRequest,db:Session = Depends(get_db)):
    to_create = Branch_master(
        branch_name = details.branch_name
    )
    db.add(to_create)
    db.commit()
    return {
        "success":True,
        "created_id":to_create.id
    }


@app.post("/vehicle")
def create_vehicle(details:CreateVehicleRequest,db:Session = Depends(get_db)):
    to_create = Vehicle_master(
        vehicle_no = details.vehicle_no,
        owner_name = details.owner_name
    )
    db.add(to_create)
    db.commit()
    return {
        "success":True,
        "created_id":to_create.id
    }

@app.get("/fetch")
def get_all_sorted_data(id:int,details:FilterFieldsRequest,db:Session = Depends(get_db)):
    return db.query(Chalan_master).filter(
        Chalan_master.created_from == details.created_from,
        Chalan_master.created_from.between(details.date_from_from,details.date_to),        
    ).order_by("amt desc")