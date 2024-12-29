from schemas.schemas import UserBase,UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List
from db.models import DbUser
from db.db_user import get_all_users  # Correctly import the function



router = APIRouter(
  prefix='/user',
  tags=['user']
)

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
  return db_user.create_user(db, request)

# Read user
# Read all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
  #return db.query(DbUser).all()
  return db_user.get_all_users(db)

# filter user
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
  return db_user.get_user(db, id)

#update user
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
  return db_user.update_user(db, id, request)


# Delete user
# Delete user
@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
  return db_user.delete_user(db, id)