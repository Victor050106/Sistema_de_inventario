from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from service.Product import ProductService
from schemas.Product import Product 
from config.database import Session



product_router = APIRouter()

@product_router.get("/product",tags=["product"],status_code=200)
def get_product():
    db = Session()
    result = ProductService(db).get_product()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@product_router.post("/product",tags=["product"], status_code=201)
def create_product(product:Product):
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(content={"message":"product create successfully","status_code":201})


@product_router.get('/product_for_id',tags=['product'],status_code=200)
def get_product_for_id(id:int):   
    db = Session()   
    result = ProductService(db).get_for_id(id)
    return JSONResponse (content=jsonable_encoder(result), status_code=200)



@product_router.put('/product{id}', tags=['product'])
def update_product(id:int,product:Product):
    db = Session()
    result = ProductService(db).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message" : "Product don't found", "status_code":404})
    ProductService(db).update_product(product)
    return JSONResponse(content={"message":"product updated succesfully", "status_code":202}, status_code=202)

@product_router.delete("/product{id}",tags = ["product"])
def delete_product(id:int):
    db = Session()
    result = ProductService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "Product don't found","status_code":404})
    ProductService(db).delete_product(id)
    return JSONResponse(content={"message":"product delete successfully", "status_code":200},status_code=200)