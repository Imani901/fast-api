from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional


app=FastAPI()

@app.get('/')
def index():
    return 'Hello world'

# @app.post('/')
# def index2():
#     return 'hi'
@app.get('/blog/all' ,tags=['blogs'])
def get_all_blogs():
    return {'message':'all blogs provided'}

@app.get('/blog/new' ,tags=['blogs'])
def get_new_blog(page = 1, page_size=10):
    return{'message':f'all {page_size} blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(id: int, comment_id: int, valid: bool = True, Username: Optional[str] = None):
    return {'message':f'Blog id {id} , comment_id {comment_id}, valid {valid}, username {Username} '}

class BlogType(str, Enum):
    short= 'short'
    story= 'story'
    howto= 'howto'

@app.get('/blog/type/{BlogType}' ,tags=['blogs'])
def get_blog_type(BlogType):
    return{'message': f'this is the blogtype {BlogType}'}    

@app.get('/blog/{id}', status_code=status.HTTP_200_OK ,tags=['blogs'])
def get_blog(id: int, response: Response):
    if id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':f'blog with {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'blog with {id}'}

