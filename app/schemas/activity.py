from datetime import datetime
from pydantic import BaseModel


class ActivityBase(BaseModel):
    description: str


class ActivityCreate(ActivityBase):
    user_id: int
    challenge_id: int | None = None


class Activity(ActivityBase):
    id: int
    timestamp: datetime
    user_id: int
    challenge_id: int | None = None

    class Config:
        from_attributes = True
