from sqlalchemy.orm import Session

from .models import Quiz
from .schemas import QuizOut


def quizzes_exist(db:Session,ids:list[int]) -> set[int]:
    """ Return a set of quiz ids in ids that exist in the database"""
    existing_quiz = db.query(Quiz).filter(Quiz.id.in_(ids)).all()
    return {quiz.id for quiz in existing_quiz}

def create_quiz(db:Session,quiz:QuizOut) -> Quiz:
    """ Create a quiz in the database"""
    db_quiz = Quiz(id=quiz.id,question=quiz.question,answer=quiz.answer,created_at=quiz.created_at)
    db.add(db_quiz)
    db.commit()
    return db_quiz

def create_quizzes(db:Session,quizzes:list[QuizOut]) -> list[Quiz]:
    """ Create quizzes in the database"""
    db_quizzes = [Quiz(id=quiz.id,question=quiz.question,answer=quiz.answer,created_at=quiz.created_at) for quiz in quizzes]
    db.add_all(db_quizzes)
    db.commit()
    return db_quizzes
