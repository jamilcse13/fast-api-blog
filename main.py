from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10,published: bool= True, sort: Optional[str]= None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch comments of blog with id = id
    return {'comments': {'comment': {'comment1', 'comment2'}}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_post(blog: Blog):
    return {'data': f'Post is created with title {blog.title} and body {blog.body}'}


# if we want to change the default localhost port
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)