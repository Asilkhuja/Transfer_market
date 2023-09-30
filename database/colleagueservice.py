from database.models import Colleague

from datetime import datetime
from database import get_db

#Добавить коллегу
def add_colleague_db(name, surname, email, phone_number, city):
    db = next(get_db())

    new_colleague = Colleague(name=name, surname=surname, email=email, phone_number=phone_number, city=city)

    db.add(new_colleague)
    db.commit()

    return 'Коллега успешно добавлен'


#Удалить коллегу
def delete_colleague_db(colleague_id):
    db = next(get_db())

    exact_colleague = db.query(Colleague).filter_by(id=colleague_id).first()

    if exact_colleague:
        db.delete(exact_colleague)
        db.commit()

        return 'Коллега успешно удален'
    return False


#Показать конкретного коллегу
def get_exact_colleague_db(colleague_id):
    db = next(get_db())

    exact_colleague = db.query(Colleague).filter_by(id=colleague_id).first()

    return exact_colleague


#Показать всех коллег
def get_all_colleagues_db():
    db = next(get_db())

    all_colleagues = db.query(Colleague).all()

    return all_colleagues