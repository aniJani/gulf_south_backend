from datetime import datetime
from pydantic import BaseModel


class TeamBase(BaseModel):
    name: str


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int
    created_at: datetime
    users: list = []

    class Config:
        from_attributes = True
