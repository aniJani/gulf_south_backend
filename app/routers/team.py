from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.team import Team, TeamCreate
from app.crud.team import get_team_by_name, create_team, get_teams
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Team)
def create_team_endpoint(team: TeamCreate, db: Session = Depends(get_db)):
    db_team = get_team_by_name(db, name=team.name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team already exists")
    return create_team(db, team)

@router.get("/", response_model=list[Team])
def read_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_teams(db, skip=skip, limit=limit)