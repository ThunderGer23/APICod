from fastapi import APIRouter

red = APIRouter()

@red.get('/test')
def getText():
    return 'holi mundo :v/'
