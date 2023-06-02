from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from service.Supplies import SuppliesService
from schemas.Supplies import Supplies
from models.Supplies import Supplies as SuppliesModel


supplies_router = APIRouter()


@supplies_router.get("/supplies",tags=["supplies"],status_code=200)
def get_supplies():
    db = Session()
    result = SuppliesService(db).get_supplies()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@supplies_router.get("/supplies_for_id",tags=["supplies"],status_code=200)
def get_supplies_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    return JSONResponse (content=jsonable_encoder(result),status_code=200)

@supplies_router.post("/supplies",tags=["supplies"],status_code=201)
def create_supplies(supplies:Supplies):
    db = Session()
    SuppliesService(db).create_supplies(supplies)
    return JSONResponse(content={"message":"supplies create successfully","status_code":201})

@supplies_router.put("/supplies{id}", tags=["supplies"])
def update_supplies(id:int,supplies:Supplies):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message": "supplies don't found", "status_code":404})
    SuppliesService(db).update_supplies(supplies)
    return JSONResponse(content={"message":"supplies update succesfully","status_code":202},status_code=202)


@supplies_router.delete("/supplies{id}",tags=["supplies"])
def delete_supplies(id:int):
    db = Session
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"supplies don't found","status_code":404})
    SuppliesService(db).delete_supplies(id)
    return JSONResponse(content={"message":"supplies delete succesfully","status_code":200},status_code=200)
