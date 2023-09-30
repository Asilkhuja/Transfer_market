from fastapi import APIRouter

from scout_conclusion import ConclusionModel, EditConclusionModel

from database.conclusionservice import change_conclusion_db, add_conclusion_db, delete_conclusion_db, get_column_conclusions

#Создать компонент
conclusion_router = APIRouter(prefix='/conclusion', tags=['Работа со скаутскими заключениями'])


#Запрос на публикацию заключение
@conclusion_router.post('/add_conclusion')
async def add_conclusion(data: ConclusionModel):
    result = add_conclusion_db(**data.model_dump())

    return {'status': 1, 'message': result}


#Запрос на изменение заключения
@conclusion_router.put('/edit_conclusion')
async def edit_conclusion(data: EditConclusionModel):
    result = change_conclusion_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Комментарий не найден'}


#Запрос на удаление заключения
@conclusion_router.delete('/delete_conclusion')
async def delete_conclusion(conclusion_id: int):
    result = delete_conclusion_db(conclusion_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': "Комментарий не найде"}


#Запрос на получение заключения к определенной колонке
@conclusion_router.get('/get_conclusions')
async def get_conclusions(column_id: int):
    result = get_column_conclusions(column_id)

    return {'status': 1, 'message': result}


#Зпрос на добавление фото для колонки
@conclusion_router.post('/add_photo')
async def add_photo():
    pass


#Запрос на удаление фотограции к колонке
@conclusion_router.delete('/delete_photo')
async def delete_photo():
    pass