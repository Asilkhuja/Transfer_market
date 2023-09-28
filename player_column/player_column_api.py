from fastapi import APIRouter

#Создать компонент
player_column_router = APIRouter(prefix='/player_column', tags=['Работа с колонками игрока'])


#Запрос на публикацию колонки
@player_column_router.post('/public_column')
async def public_column():
    pass


#Запрос на изменение текста
@player_column_router.post('/change_column')
async def change_column():
    pass


#Запрос на удаление колонки
@player_column_router.delete('/delete_column')
async def delete_column():
    pass


#Запрос на получение колонки
@player_column_router.get('/get_column')
async def get_column():
    pass


#Зпрос на добавление фото для колонки
@player_column_router.post('/add_photo')
async def add_photo():
    pass


#Запрос на удаление фотограции к колонке
@player_column_router.delete('/delete_photo')
async def delete_photo():
    pass