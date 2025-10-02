from fastapi import FastAPI



app=FastAPI()

@app.get('/')
def index():
    return 'Hello world'

# @app.post('/')
# def index2():
#     return 'hi'

