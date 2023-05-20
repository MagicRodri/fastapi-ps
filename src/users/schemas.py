import json
import uuid

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(..., example="testuser")


class UserCreate(UserBase):
    access_token: uuid.UUID = Field(default_factory=uuid.uuid4)


class UserIn(BaseModel):
    id: int = Field(..., example=1)
    access_token: uuid.UUID = Field(
        ..., example="123e4567-e89b-12d3-a456-426614174000")

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class User(UserCreate):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
