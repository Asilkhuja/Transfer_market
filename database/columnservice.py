from datetime import datetime

from database.models import Player_Column, PlayerPhoto
from database import get_db

#Добавить колонку
def add_column_db(agent_id, column_text):
    db = next(get_db())

    #Создать объект для БД
    new_column = Player_Column(agent_id=agent_id, column_text=column_text,
                               publish_date=datetime.now())

    #Добавить запись в БД
    db.add(new_column)
    db.commit()

    return 'Добавлено успешно'


#Добавить фото к колонке
def add_column_photo_db(column_id, photo):
    db = next(get_db())
    new_column_photo = PlayerPhoto(column_id=column_id, column_photo=photo)

    db.add(new_column_photo)
    db.commit()

    return 'Фотографи загружена'


#Изменить колонку
def edit_column_db(column_id, agent_id, new_text):
    db = next(get_db())
    exact_column = db.query(Player_Column).filter_by(id=column_id, agent_id=agent_id).first()

    if exact_column:
        exact_column.column_text = new_text
        db.commit()

        return 'Успешно изменена'

    return False


#Удалить колонку
def delete_column_db(column_id):
    db = next(get_db())
    exact_column = db.query(Player_Column).filter_by(id=column_id).first()

    if exact_column:
        db.delete(exact_column)
        db.commit()

        return 'Колонка удалена успешно'

    return False

#Получить все колонки
def get_all_columns():
    db = next(get_db())

    all_columns = db.query(Player_Column).all()

    return all_columns


#Получить определенную колонку
def get_exact_column(column_id):
    db = next(get_db())
    exact_column = db.query(Player_Column).filter_by(id=column_id).first()
    if exact_column:
        return exact_column

    return False