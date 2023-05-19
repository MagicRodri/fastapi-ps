from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(..., example="testuser")
    email: EmailStr = Field(..., example="example@test.com")
    

class UserCreate(UserBase):
    password: str = Field(..., example="password")

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True