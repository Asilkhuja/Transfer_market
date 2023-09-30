from pydantic import BaseModel

#Валидатор добавления коллеги
class AddColleagueModel(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    city: str