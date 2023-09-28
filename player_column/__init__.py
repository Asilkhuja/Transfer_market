from pydantic import BaseModel


#Валидатор публикации колонки
class PublicColumnModel(BaseModel):
    agent_id: int
    column_text: str


#Валидатор изменения текста к колонке
class EditColumnModel(BaseModel):
    column_id: int
    new_text: str
    agent_id: int