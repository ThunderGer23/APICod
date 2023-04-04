from fastapi import APIRouter
from helpers.model import new_model as model
from helpers.inter import interprete
from models.red import Red
from os import environ as env
from notigram import ping

red = APIRouter()

@red.post('/test', response_model= list[str], tags=["Cod"])
def postText(red: Red):
    # ping('daa39d53-6283-47a1-b945-b7ee6528dde0', 'Iniciando analisis de código')
    analisis = model.predict(red.code)
    # ping('daa39d53-6283-47a1-b945-b7ee6528dde0', 'Interpretación lista')
    return interprete(analisis)
