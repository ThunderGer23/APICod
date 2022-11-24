from fastapi import APIRouter
from helpers.model import new_model as model
from helpers.inter import interprete
from models.red import Red
from os import environ as env
from notigram import ping

red = APIRouter()

@red.get('/test')
def getText(red: Red):
    ping(env['TOKERN'], 'Iniciando analisis de código')
    analisis = model.predict(red.code)
    ping(env['TOKERN'], 'Interpretación lista')
    return interprete(analisis)
