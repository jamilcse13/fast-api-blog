from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Jamil', 'age': 27}}

@app.get('/about')
def about():
    return {'data': {'about page'}}