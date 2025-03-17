from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.statistics import get_user_statistics, get_challenge_statistics

router = APIRouter()


# stats for user and challenge
@router.get("/statistics/user/{user_id}")
def user_statistics(user_id: int, db: Session = Depends(get_db)):
    stats = get_user_statistics(db, user_id)
    if stats is None:
        raise HTTPException(status_code=404, detail="Statistics not found")
    return stats


@router.get("/statistics/challenge/{challenge_id}")
def challenge_statistics(challenge_id: int, db: Session = Depends(get_db)):
    stats = get_challenge_statistics(db, challenge_id)
    if stats is None:
        raise HTTPException(status_code=404, detail="Statistics not found")
    return stats
