import datetime

from pydantic import BaseModel


# Question 스키마
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    
    # Question 모델의 항목일드 자동을 Question 스키마로 매핑
    class Config:
        orm_mode = True

