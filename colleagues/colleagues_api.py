from fastapi import APIRouter, Body

#Создать компонент
colleagues_router = APIRouter(prefix='/colleagues', tags=['Управление списком коллег'])


#Зпрос на добавление коллеги
@colleagues_router.post('/add_colleague')
async def add_colleague(agent_id: int = Body(),
                    colleague_id: int = Body()):
    pass

#Запрос на удаление коллеги
@colleagues_router.delete('/delete_colleague')
async def delete_colleague(colleague_id: int, agent_id: int):
    pass


#Запрос на получение списка коллег
@colleagues_router.get('/get_all_colleagues')
async def get_all_colleagues(agent_id: int):
    pass


#Запрос на получение информации о конкретном коллеге
@colleagues_router.get('/get_exact_colleague')
async def get_exact_colleague(colleague_id: int):
    pass

#python41Potok