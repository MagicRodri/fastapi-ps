from db.base import Base
from sqlalchemy import Column, DateTime, Integer, String


class Quiz(Base):

    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
