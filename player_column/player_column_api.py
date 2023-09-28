from fastapi import APIRouter, UploadFile, Body

from player_column import PublicColumnModel, EditColumnModel


#Создать компонент
player_column_router = APIRouter(prefix='/player_column', tags=['Работа с колонками игрока'])


#Запрос на публикацию колонки
@player_column_router.post('/public_column')
async def public_column(data: PublicColumnModel):
    pass


#Запрос на изменение текста
@player_column_router.post('/change_column')
async def change_column(data: EditColumnModel):
    pass


#Запрос на удаление колонки
@player_column_router.delete('/delete_column')
async def delete_column(column_id: int, agent_id: int):
    pass


#Запрос на получение колонки
@player_column_router.get('/get_column')
async def get_column():
    pass


#Зпрос на добавление фото для колонки
@player_column_router.post('/add_photo')
async def add_photo(agent_id: int,
                    column_id: int = Body(),
                    photo_file: UploadFile = None):
    pass


#Запрос на удаление фотограции к колонке
@player_column_router.delete('/delete_photo')
async def delete_photo(photo_id: int, agent_it: int):
    pass