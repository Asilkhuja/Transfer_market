from pydantic import BaseModel


#Валидатор для регистрации
class AgentRegisterModel(BaseModel):
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    password: str



#Валидатор для логина
class AgentLoginModel(BaseModel):
    email: str
    password: str


#Валидатор для изменения данных агента
class AgentChangeModel(BaseModel):
    agent_id: int
    edit_info: str
    new_info: str

