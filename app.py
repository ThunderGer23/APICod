from fastapi import FastAPI
from routes.red import red

app = FastAPI()

app.include_router(red)