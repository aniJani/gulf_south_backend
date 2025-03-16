from datetime import datetime
from pydantic import BaseModel


class ChallengeBase(BaseModel):
    title: str
    description: str | None = None


class ChallengeCreate(ChallengeBase):
    end_date: datetime


class Challenge(ChallengeBase):
    id: int
    start_date: datetime
    end_date: datetime

    class Config:
        from_attributes = True
