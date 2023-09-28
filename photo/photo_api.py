from fastapi import APIRouter, UploadFile


photo_router = APIRouter(prefix='/photos', tags=["Agent's photos"])


#Получить все или определенное фото (для player_column)
@photo_router.get('/get_photo')
async def get_all_or_exact_photo(photo_id: int = None):
    pass

#Добавление фото (для агента)
@photo_router.post('/add_photo')
async def add_photo(photo_file: UploadFile, agent_id: int):
    #Сохранить локально фото
    with open(f'media/{photo_file.filename}', 'wb') as file:
        agent_photo = await photo_file.read()

        file.write(agent_photo)

    return {'message': 'сохранил'}


#Изменить фото (для агента)
@photo_router.put('/edit_photo')
async def edit_photo(photo_id: int, new_photo_file):
    pass


#Удалить фото
@photo_router.delete('/delete_photo')
async def delete_photo(photo_id: int):
    pass
