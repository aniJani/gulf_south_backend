from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.leaderboards import (
    get_challenge_leaderboard,
    get_team_leaderboard,
    get_user_leaderboard,
)

router = APIRouter()


@router.get("/leaderboards/challenges/{challenge_id}")
def challenge_leaderboard(challenge_id: int, db: Session = Depends(get_db)):
    leaderboard = get_challenge_leaderboard(db, challenge_id)
    return leaderboard


@router.get("/leaderboards/teams")
def team_leaderboard(db: Session = Depends(get_db)):
    leaderboard = get_team_leaderboard(db)
    return leaderboard


@router.get("/leaderboards/users")
def users_leaderboard(limit: int = 10, db: Session = Depends(get_db)):
    leaderboard = get_user_leaderboard(db, limit)
    return leaderboard
