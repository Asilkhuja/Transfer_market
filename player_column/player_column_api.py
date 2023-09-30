from fastapi import APIRouter, UploadFile, Body

from player_column import PublicColumnModel, EditColumnModel

from database.columnservice import add_column_db, add_column_photo_db, get_all_columns_db, get_exact_column,\
    delete_column_db, edit_column_db

#Создать компонент
player_column_router = APIRouter(prefix='/player_column', tags=['Работа с колонками игрока'])


#Запрос на публикацию колонки
@player_column_router.post('/public_column')
async def public_column(data: PublicColumnModel):
    result = add_column_db(**data.model_dump())

    return {'status': 1, 'message': result}


#Запрос на изменение текста
@player_column_router.post('/change_column')
async def change_column(data: EditColumnModel):
    result = edit_column_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Колонка не найдена'}


#Запрос на удаление колонки
@player_column_router.delete('/delete_column')
async def delete_column(column_id: int):
    result = delete_column_db(column_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Колонка не найдена'}


#Запрос на получение колонки
@player_column_router.get('/get_exact_column')
async def get_exact_column(column_id: int):
    result = get_exact_column(column_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Колонка не найдена'}


#Запрос на получение всех колонок
@player_column_router.get('/get_all_columns')
async def get_all_columns():
    result = get_all_columns_db()

    return {'status': 1, 'message': result}


#Зпрос на добавление фото для колонки
@player_column_router.post('/add_photo')
async def add_photo(agent_id: int = Body(),
                    column_id: int = Body(),
                    photo_file: UploadFile = None):
    photo_path = f'/media/{photo_file.filename}'

    try:
        #Сохранение фотографии в папку media
        with open(f'media/{photo_file.filename}', 'wb') as file:
            agent_photo = await photo_file.read()

            file.write(agent_photo)

        #Сохранение ссылки к фотографии в базу
        result = add_column_photo_db(column_id=column_id,
                                 photo=photo_path)

    except Exception as error:
        result = error

    return {'status': 1, 'message': result}