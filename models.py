from sqlalchemy import Column, Integer, String, Text, DateTime , ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# Question 모델
class Question(Base):
    __tablename__ = "question"

    id = Column(Integer,primary_key=True)
    #String 글자가 제한
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

# Answer 모델
class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    # question.id 는 question 테이블의 id 컬럼을 의미힌다.
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answer")
