from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
import databases
import model
import schema
from hashing import Hash

def create(request:schema.User,db:Session=Depends(databases.get_db)):
    new_user=model.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def single_user(id:int,db:Session=Depends(databases.get_db)):
    user=db.query(model.User).filter(model.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} is not available')
    return user
