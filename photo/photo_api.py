from fastapi import APIRouter, UploadFile


photo_router = APIRouter(prefix='/photos', tags=["Agent's photos"])

from database.agentservice import add_profile_photo_db, delete_profile_photo_db

#Добавление фото (для агента)
@photo_router.post('/add_photo')
async def add_photo(photo_file: UploadFile, agent_id: int):
    #Сохранить локально фото
    with open(f'media/{photo_file.filename}', 'wb') as file:
        agent_photo = await photo_file.read()

        file.write(agent_photo)

    result = add_profile_photo_db(agent_id, photo=f'/media/{photo_file.filename}')

    return {'status': 1, 'message': result}


#Изменить фото (для агента)
@photo_router.put('/edit_photo')
async def edit_photo(agent_id: int, new_photo_file: UploadFile):
    # Сохранить локально фото
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        agent_photo = await new_photo_file.read()

        file.write(agent_photo)

    result = add_profile_photo_db(agent_id, photo=f'/media/{new_photo_file.filename}')

    return {'status': 1, 'message': result}


#Удалить фото
@photo_router.delete('/delete_photo')
async def delete_photo(agent_id: int):
    result = delete_profile_photo_db(agent_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Агент не найден'}