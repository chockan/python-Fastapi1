from fastapi import APIRouter,Response,status
from enum import Enum
from typing import Optional

router=APIRouter(
    prefix='/blo',
    tags=['getting']
)


@router.get('/blog/{id}')
def blog(id:int):
    return {'return':f'{id}'}


class BlogType(str,Enum):
    short="1"
    long='2'

@router.get('/blogtype/{type}',tags=['comment'])
def blogtype(type:BlogType):
    return {"data":f'{type}'}

@router.get('/blogab/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

@router.get('/blogget/{id}',status_code=status.HTTP_200_OK)
def blogget(id:int,response:Response):
    if id>5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'error':f'{id} not found'}
    
    else:
        response.status_code=status.HTTP_200_OK
        return {'message':f'{id}'}
    


