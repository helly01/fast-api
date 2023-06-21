from fastapi import FastAPI
from typing import Union, Optional
from pydantic import BaseModel

# http://127.0.0.1:8000/openapi.json
# openapi.json authomatically generate JSON schema with the description of all api

# instance of fastapi
app = FastAPI()
# FastAPI is a Python class that provides all the functionality for your API.
# FastAPI is a class that inherits directly from Starlette.



@app.get('/blog') 
# path/endpoint/route
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # http://127.0.0.1:8000/blog?limit=10&published=false
    if published:
    # only get 10 published blog
        return {'data': f'{limit} published blogs from DB'}
    else:
        return {'data': f'{limit} blogs from DB'}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished'}


# dynamic routing
@app.get('/blog/{id}')
def show(id: int, limit=10):
    # consider limit as a query parameter
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
# Declare a variable as a int
def comments(id: int):
    # fetch comment with blog id =id
    return {'data': {'1', '2'}}


# A Pydantic model
class Blog(BaseModel):
    # this is now model because we extended basemodel
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with {request.title}'}