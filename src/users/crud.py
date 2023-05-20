from sqlalchemy.orm import Session

from .models import Record, User
from .schemas import UserCreate, UserIn


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(username=user.username, access_token=user.access_token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_access_token(db: Session, access_token: str):
    return db.query(User).filter(User.access_token == access_token).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user(db: Session, user_in: UserIn):
    return db.query(User).filter(
        User.id == user_in.id,
        User.access_token == user_in.access_token).first()


def create_record(db: Session, user: User, file: str):
    db_record = Record(user=user.id, file=file)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def get_record(db: Session, user_id: int, record_id: int):
    return db.query(Record).filter(Record.id == record_id,
                                   Record.user == user_id).first()
