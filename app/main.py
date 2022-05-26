from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.apis.routes import routers
from app.core.container import Container

app = FastAPI()

container = Container()

@app.get('/')
def read_root():
    return 'hello fastapi'

app.include_router(routers)
