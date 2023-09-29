from database.models import Agent

from database.models import Agent
from database import get_db


#Регистрация агента
def register_agent_db(name, surname, email, phone_number, city, password):
    db = next(get_db())

    checker = db.query(Agent).filter_by(email=email).first()

    if checker:
        return False

    new_agent = Agent(name=name, surname=surname,
                      email=email, phone_number=phone_number,
                      city=city, password=password)

    db.add(new_agent)
    db.commit()

    return 'Агент успешно зарегистрирован'


#Вход в аккаунт
def login_agent_db(email, password):
    db = next(get_db())

    checker = db.query(Agent).filter_by(email=email).first()

    if checker:
        if checker.password == password:
            return checker

        elif checker.password != password:
            return 'Неверный пароль'

    return 'Ошибка в данных'


#Добавить фото профиля
def add_profile_photo_db(agent_id, photo):
    db = next(get_db())

    checker = db.query(Agent).filter_by(id=agent_id).first()

    if checker:
        checker.profile_photo = photo
        db.commit()

        return 'Фото профиля успешно добавлено'

    return False


#Изменить данные


#Удалить фото профиля
def delete_profile_photo_db(agent_id):
    db = next(get_db())

    checker = db.query(Agent).filter_by(id=agent_id).first()

    if checker:
        checker.profile_photo = 'None'
        db.commit()

        return 'Фото профиля удалено'

    return False


#Получить всех агентов
def get_all_agents_db():
    db = next(get_db())

    all_agents = db.query(Agent).all()

    return all_agents


#Получить информацию про определенного агента
def get_exact_agent_db(agent_id):
    db = next(get_db())

    exact_agent = db.query(Agent).filter_by(id=agent_id).first()

    return exact_agent