from fastapi import APIRouter

from agent import AgentLoginModel, AgentRegisterModel, AgentChangeModel

from database.agentservice import login_agent_db, register_agent_db, get_exact_agent_db, get_all_agents_db


#Создать компонент
agent_router = APIRouter(prefix='/agent', tags=['Управление аккаунтом агента'])

#Запрос на вход в аккаунт
@agent_router.post('/login')
async def login_agent(data: AgentLoginModel):
    result = login_agent_db(**data.model_dump())

    return {'status': 1, 'message': result}


#Запрос на регистрацию
@agent_router.post('/register')
async def register_agent(data: AgentRegisterModel):
    result = register_agent_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Агент с такой почтой уже есть в БД'}


#Запрос на изменение информации пользователя
@agent_router.put('/change_info')
async def change_info(data: AgentChangeModel):
    pass


#Запрос на получение информации о пользователе
@agent_router.get('/get_agent')
async def get_agent(agent_id: int = 0):
    if agent_id == 0:
        result = get_all_agents_db()

        return {'status': 1, 'message': result}

    else:
        result = get_exact_agent_db(agent_id)

        return {'status': 1, 'message': result}
