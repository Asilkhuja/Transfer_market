from pydantic import BaseModel


#Валидатор заключения
class ConcludionModel(BaseModel):
    sonclusion_text: str
    agent_id: int


#Валидатор на изменение заключения
class EditConclusionModel(BaseModel):
    new_text: str
    conclusion_id: int


