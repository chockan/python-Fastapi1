from fastapi import FastAPI,status,Response
from enum import Enum
from typing import Optional
from routers import get,gpost
from routers import user
from routers import article
from db.database import engine
from db import models
app=FastAPI()

app.include_router(get.router)
app.include_router(gpost.router)
app.include_router(article.router)
app.include_router(user.router)

@app.get('/')
def abc():
    return 'hello'


models.Base.metadata.create_all(engine)
