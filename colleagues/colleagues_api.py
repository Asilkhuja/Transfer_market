from fastapi import APIRouter, Body
from colleagues import AddColleagueModel

from database.colleagueservice import add_colleague_db, get_exact_colleague_db,\
    get_all_colleagues_db, delete_colleague_db

#Создать компонент
colleagues_router = APIRouter(prefix='/colleagues', tags=['Управление списком коллег'])


#Зпрос на добавление коллеги
@colleagues_router.post('/add_colleague')
async def add_colleague(data: AddColleagueModel):
    result = add_colleague_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Коллега с такой почтой уже есть в базе'}

#Запрос на удаление коллеги
@colleagues_router.delete('/delete_colleague')
async def delete_colleague(colleague_id: int):
    result = delete_colleague_db(colleague_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Коллега не найден'}


#Запрос на получение списка коллег
@colleagues_router.get('/get_all_colleagues')
async def get_all_colleagues(agent_id: int):
    result = get_all_colleagues_db()

    return {'status': 1, 'message': result}


#Запрос на получение информации о конкретном коллеге
@colleagues_router.get('/get_exact_colleague')
async def get_exact_colleague(colleague_id: int):
    result = get_exact_colleague_db(colleague_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Коллега не найден'}

