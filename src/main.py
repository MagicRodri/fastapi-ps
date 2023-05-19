from api.v1 import router as api_v1_router
from core.config import settings
from fastapi import FastAPI, Request

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api(request:Request):
    # print(request.values)
    return {"detail": "Hello Mom!"}

app.include_router(api_v1_router, prefix=settings.API_V1_STR)
