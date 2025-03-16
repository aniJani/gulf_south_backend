from datetime import datetime, date
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    full_name: str | None = None
    password: str | None = None


class User(UserBase):
    id: int
    created_at: datetime
    weekly_challenge_ids: list[int] | None = None
    weekly_challenge_week: date | None = None

    class Config:
        from_attributes = True
