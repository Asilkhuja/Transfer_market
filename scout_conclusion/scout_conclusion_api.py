from fastapi import APIRouter

from scout_conclusion import ConclusionModel, EditConclusionModel


#Создать компонент
conclusion_router = APIRouter(prefix='/comment', tags=['Работа со скаутскими заключениями'])


#Запрос на публикацию заключение
@conclusion_router.post('/add_conclusion')
async def add_conclusion(data: ConclusionModel):
    pass


#Запрос на изменение заключения
@conclusion_router.put('/edit_conclusion')
async def edit_conclusion(data: EditConclusionModel):
    pass


#Запрос на удаление заключения
@conclusion_router.delete('/delete_conclusion')
async def delete_conclusion(conclusion_id: int):
    pass


#Запрос на получение заключения к определенной колонке
@conclusion_router.get('/get_conclusions')
async def get_conclusions(column_id: int):
    pass


#Зпрос на добавление фото для колонки
@conclusion_router.post('/add_photo')
async def add_photo():
    pass


#Запрос на удаление фотограции к колонке
@conclusion_router.delete('/delete_photo')
async def delete_photo():
    pass