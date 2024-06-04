from fastapi import FastAPI
import redis


app = FastAPI()

#comments here

@app.get('/')
def read_root():
    return {'hello': 'wolrd 123'}
