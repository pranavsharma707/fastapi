from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
import schema
import databases
import model
from repository.blog import *

router=APIRouter(
    prefix='/blog',
    tags=['blogs']
)

#now we take the @app.get of blog  from main.py and instead of @app.get we write @router.get and now have to bring db dunction from main.py to database.py

@router.get('/',response_model=List[schema.ShowBlog])
def all(db:Session=Depends(databases.get_db)):
    return get_all(db)
    
#now we have to register that router in main.py
@router.get('/{id}',status_code=200,response_model=schema.ShowBlog)
def show(id,db:Session=Depends(databases.get_db)):
    return single(id,db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_data(request:schema.Blog,db:Session=Depends(databases.get_db)):
    return data_created(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id,db:Session=Depends(databases.get_db)):
    return data_delete(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schema.Blog,db:Session=Depends(databases.get_db)):
  return update_data(id,request,db)