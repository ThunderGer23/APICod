from fastapi import APIRouter
from helpers.model import new_model as model
from helpers.inter import interprete
from models.red import Red
from os import environ as env
from notigram import ping

red = APIRouter()

@red.post('/test', response_model= list[str], tags=["Cod"])
def postText(red: Red):
    ping(env['TOKEN'], 'Iniciando analisis de código')
    analisis = model.predict(red.code)
    ping(env['TOKEN'], 'Interpretación lista')
    return interprete(analisis)
