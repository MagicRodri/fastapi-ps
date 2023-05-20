import requests
from db.session import get_db
from fastapi import APIRouter, Depends
from quizzes import crud, schemas
from sqlalchemy.orm import Session

router = APIRouter(prefix='/quizzes', tags=['quizzes'])

@router.post('/random',response_model=list[schemas.QuizOut])
def get_random_quizzes(payload:schemas.QuizCreate, db: Session = Depends(get_db)):
    """
        Get questions_num random quizzes from https://jservice.io/api/
    """
    quizzes = []
    questions_num = payload.questions_num

    if questions_num <= 0:
        return quizzes

    endpoint = 'https://jservice.io/api/random?count={count}'
    while len(quizzes) < questions_num:
        count = min(questions_num - len(quizzes),100) # jservice.io only allows 100 quizzes per request
        response = requests.get(endpoint.format(count=count))
        data = response.json()

        existing_quizzes_ids_set = crud.quizzes_exist(db,[quiz['id'] for quiz in data])
        new_quizzes = [schemas.QuizOut(**quiz) for quiz in data if quiz['id'] not in existing_quizzes_ids_set]
        db_quizzes = crud.create_quizzes(db,new_quizzes)
        quizzes.extend(db_quizzes)

    return quizzes