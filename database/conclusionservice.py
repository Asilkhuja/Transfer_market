from datetime import datetime

from database.models import Scout_conclusion
from database import get_db

#Опубликовать заключение
def add_conclusion_db(column_id, text, agent_id):
    db = next(get_db())

    new_conclusion = Scout_conclusion(column_id=column_id, conclusion_text=text, agent_id=agent_id)

    db.add(new_conclusion)
    db.commit()

    return 'Заключение успешно добавлено'


#Удалить заключение
def delete_conclusion_db(conclusion_id):
    db = next(get_db())

    exact_conclusion = db.query(Scout_conclusion).filter_by(id=conclusion_id).first()

    if exact_conclusion:
        db.delete(exact_conclusion)
        db.commit()

        return 'Заключение успешно удалено'
    return False


#Изменить определенное заключение
def change_conclusion_db(conclusion_id, new_text):
    db = next(get_db())

    exact_conclusion = db.query(Scout_conclusion).filter_by(id=conclusion_id,).first()

    if exact_conclusion:
        exact_conclusion.conclusion_text = new_text
        db.commit()

        return 'Заключение успешно изменен'

    return False


#Получить все заключения отельной колонки
def get_column_conclusions(column_id):
    db = next(get_db())

    exact_column_conclusions = db.query(Scout_conclusion).filter_by(column_id=column_id).all()

    return exact_column_conclusions