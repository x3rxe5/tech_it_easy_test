from datetime import date, datetime
from pydantic import BaseModel

class CreateBillRequest(BaseModel):
    bilty_no:int
    bill_type:int
    amt:int
    chalan_id:int

class CreateChalanRequest(BaseModel):
    chalan_no:int    
    chalan_date:str
    inwarded:int
    station_from:int
    station_to:int
    vehicle_id:int
    created_from:int

class CreateVehicleRequest(BaseModel):
    vehicle_no:int
    owner_name:str

class CreateBranchRequest(BaseModel):    
    branch_name:str

class FilterFieldsRequest(BaseModel):
    created_from:int
    date_from:datetime
    date_to:datetime
    vehicle_no:str

    