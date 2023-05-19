from fastapi import APIRouter
from users.routers import router as user_router

router = APIRouter()

@router.get("/")
def hello_api_v1():
    return {"detail": "Hello API V1!"}

router.include_router(user_router)