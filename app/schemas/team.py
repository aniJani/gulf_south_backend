from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class UserBase(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class TeamBase(BaseModel):
    name: str
    description: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class TeamUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Team(TeamBase):
    id: int
    created_at: datetime
    users: List[UserBase] = []

    class Config:
        from_attributes = True
