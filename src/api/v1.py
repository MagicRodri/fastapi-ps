from fastapi import APIRouter
from quizzes.routers import router as quizzes_router
from users.routers import router as users_router

router = APIRouter()

@router.get("/")
def hello_api_v1():
    return {"detail": "Hello API V1!"}

router.include_router(users_router)
router.include_router(quizzes_router)