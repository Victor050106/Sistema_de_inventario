from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder


from service.genres import GenresService
from schemas.genres import Genres 
from config.database import Session



genres_router = APIRouter()

@genres_router.get('/genres_hello', tags=['genres'], status_code=200)
def get_genres_hello():
    """function to check the route"""
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')


@genres_router.get('/genres', tags = ['genres'], status_code=200)
def get_genres():
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)


@genres_router.get('/genres_for_id', tags=['genres'], status_code=200)
def get_genres_for_id(id:int):
    db = Session()
    result = GenresService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres(genres:Genres):
    db = Session()
    GenresService(db).create_genre(genres)
    return JSONResponse(content={"message":"genre created successfully",'status_code':201}, status_code=201)

#creamos un get que trae un solo genero por id 

# para el genres delete debemos verificar que el id existe y despues ese genero lo eliminamos


