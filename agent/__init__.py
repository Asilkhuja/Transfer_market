from pydantic import BaseModel


#Валидатор для регистрации
class AgentRegisterModel(BaseModel):
    agent_name: str
    agent_surname: str
    phone_number: int
    mail: str
    city: str
    password: str



#Валидатор для логина
class AgentLoginModel(BaseModel):
    agent_mail: str
    password: str


#Валидатор для изменения агента
class AgentChangeModel(BaseModel):
    agent_id: int
    new_info: str

