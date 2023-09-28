from fastapi import APIRouter

from agent import AgentLoginModel, AgentRegisterModel, AgentChangeModel

#Создать компонент
agent_router = APIRouter(prefix='/agent', tags=['Управление аккаунтом агента'])

#Запрос на вход в аккаунт
@agent_router.post('/login')
async def login_agent(data: AgentLoginModel):
    pass


#Запрос на регистрацию
@agent_router.post('/register')
async def register_agent(data: AgentRegisterModel):
    pass


#Запрос на изменение информации пользователя
@agent_router.put('/change_info')
async def change_info(data: AgentChangeModel):
    pass


#Запрос на получение информации о пользователе
@agent_router.get('/get_agent')
async def get_agent(agent_id: int):
    pass