from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.team import Team, TeamCreate, UserBase
from app.crud.team import (
    get_team_by_name,
    create_team,
    get_teams,
    add_member_to_team,
    get_team_members,
)
from app.database import get_db

router = APIRouter()


# Create a new team
@router.post("/", response_model=Team)
def create_team_endpoint(team: TeamCreate, db: Session = Depends(get_db)):
    db_team = get_team_by_name(db, name=team.name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team already exists")
    return create_team(db, team)


# Get all teams
@router.get("/", response_model=list[Team])
def read_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_teams(db, skip=skip, limit=limit)


# Add a member to a team
@router.post("/{team_id}/members")
def add_team_member(team_id: int, user_id: int, db: Session = Depends(get_db)):
    team = add_member_to_team(db, team_id, user_id)
    if not team:
        raise HTTPException(status_code=400, detail="Unable to add member")
    return {"message": "Member added", "team": team}


# Get all members of a team
@router.get("/{team_id}/members", response_model=List[UserBase])
def get_team_members_endpoint(team_id: int, db: Session = Depends(get_db)):
    members = get_team_members(db, team_id)
    return members
