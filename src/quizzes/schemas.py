from datetime import datetime

from pydantic import BaseModel, Field


class QuizCreate(BaseModel):
    questions_num:int = Field(...,example=10)

class QuizOut(BaseModel):
    id:int
    question:str
    answer:str
    created_at:datetime

    class Config:
        orm_mode = True