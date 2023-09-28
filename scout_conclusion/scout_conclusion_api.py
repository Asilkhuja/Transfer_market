from fastapi import APIRouter


#Создать компонент
conclusion_router = APIRouter(prefix='/comment', tags=['Работа с заключениями'])


#Запрос на публикацию заключение
@conclusion_router.post('/add_conclusion')
async def add_conclusion():
    pass


#Запрос на изменение заключения
@conclusion_router.put('/edit_conclusion')
async def edit_conclusion():
    pass


#Запрос на удаление заключения
@conclusion_router.delete('/delete_conclusion')
async def delete_conclusion():
    pass


#Запрос на получение заключения к определенной колонке
@conclusion_router.get('/get_conclusions')
async def get_conclusions():
    pass


#Зпрос на добавление фото для колонки
@conclusion_router.post('/add_photo')
async def add_photo():
    pass


#Запрос на удаление фотограции к колонке
@conclusion_router.delete('/delete_photo')
async def delete_photo():
    pass