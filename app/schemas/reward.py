from datetime import datetime
from pydantic import BaseModel


class RewardBase(BaseModel):
    reward_type: str
    description: str | None = None
    points: int


class RewardCreate(RewardBase):
    user_id: int


class Reward(RewardBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True
