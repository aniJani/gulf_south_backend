from datetime import datetime
from pydantic import BaseModel


class ActivityBase(BaseModel):
    title: str
    description: str | None = None
    points: int = 0


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    points: int | None = None
    is_completed: bool | None = None


class Activity(ActivityBase):
    id: int
    is_completed: bool
    completed_at: datetime | None = None
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True
