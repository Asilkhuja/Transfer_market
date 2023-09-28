from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from photo.photo_api import photo_router
from scout_conclusion.scout_conclusion_api import conclusion_router
from player_column.player_column_api import player_column_router
from agent.agent_api import agent_router



app = FastAPI(docs_url='/')

#Регистрация компонентов
app.include_router(agent_router)
app.include_router(player_column_router)
app.include_router(photo_router)
app.include_router(conclusion_router)

#Добавление ссылки для открытия локальных файлов
app.mount(path='/media', app=StaticFiles(directory='media'))

@app.get('/hello')
async def hello():
    return {'message': 'Hello world'}