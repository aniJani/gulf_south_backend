from datetime import datetime
from pydantic import BaseModel


class ChallengeBase(BaseModel):
    title: str
    description: str | None = None
    points: int = 0
    start_date: datetime | None = None
    end_date: datetime | None = None
    is_active: bool = True


class ChallengeCreate(ChallengeBase):
    pass


class ChallengeUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    points: int | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    is_active: bool | None = None


class Challenge(ChallengeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
