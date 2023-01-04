import datetime

from pydantic import BaseModel
from typing import List

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: List[Answer] = []

    class Config:
        orm_mode = True
