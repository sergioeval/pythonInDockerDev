from fastapi import FastAPI
import redis


app = FastAPI()


@app.get('/')
def read_root():
    return {'hello': 'wolrd 123'}
