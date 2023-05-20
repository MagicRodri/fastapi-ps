import mimetypes
import uuid
from pathlib import Path

import aiofiles
from core.config import SRC_DIR, settings
from db.session import get_db
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from users import crud, schemas

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    return crud.create_user(db=db,
                            user=schemas.UserCreate(username=user.username))


@router.get("/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return db_user


@router.post("/record")
async def upload_user_record(payload: schemas.UserIn,
                             file: UploadFile = File(...,
                                                     media_type='audio/x-wav'),
                             db: Session = Depends(get_db)):
    """Upload a WAV audio record for a user."""
    db_user = crud.get_user(db=db, user_in=payload)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    mime_type, _ = mimetypes.guess_type(file.filename)
    if mime_type != "audio/x-wav":
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only WAV audio files are allowed.")

    contents = await file.read()
    file_path = Path(settings.MEDIA_ROOT) / 'records' / file.filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(file_path, mode="wb") as f:
        await f.write(contents)
    db_record = crud.create_record(db=db,
                                   user=db_user,
                                   file=str(file_path.relative_to(SRC_DIR)))
    download_url = f"{settings.API_V1_STR}/users/records/{db_record.id}/{db_user.id}"
    return {"url": download_url}


@router.get("records/{id}/{user_id}")
def download_user_record(record_id: uuid.UUID,
                         user_id: int,
                         db: Session = Depends(get_db)):
    """Download a WAV audio record for a user."""
    db_record = crud.get_record(db=db, user_id=user_id, record_id=record_id)
    if db_record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return FileResponse(db_record.file,
                        media_type='audio/x-wav',
                        filename=db_record.filename)
