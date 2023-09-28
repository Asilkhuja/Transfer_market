from fastapi import APIRouter


#Создать компонент
agent_router = APIRouter(prefix='/agent', tags=['Управление пользователями'])

#Запрос на вход в аккаунт
@agent_router.post('/login')
async def login_agent():
    pass


#Запрос на регистрацию
@agent_router.post('/register')
async def regiser_agent():
    pass


#Запрос на изменение информации пользователя
@agent_router.put('/change_info')
async def change_info():
    pass


#Запрос на получение информации о пользователе
@agent_router.get('/get_agent')
async def get_agent():
    pass