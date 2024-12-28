from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router=APIRouter(
    prefix='/gpo',
    tags=['gp']
)

@router.get('/gto')
def gtoab():
    return 'gtopost'

class BlogModel(BaseModel):
    name:str
    email:str
    published:Optional[bool]

@router.post('/new')
def abcdef(blog:BlogModel):
    return {'data':blog}