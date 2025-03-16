from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.challenge import Challenge, ChallengeCreate
from app.crud.challenge import get_challenge_by_title, create_challenge, get_challenges, get_weekly_challenge_options
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Challenge)
def create_challenge_endpoint(challenge: ChallengeCreate, db: Session = Depends(get_db)):
    db_challenge = get_challenge_by_title(db, title=challenge.title)
    if db_challenge:
        raise HTTPException(status_code=400, detail="Challenge already exists")
    return create_challenge(db, challenge)

@router.get("/", response_model=list[Challenge])
def read_challenges(weekly: bool = False, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    if weekly:
        return get_weekly_challenge_options(db)
    return get_challenges(db, skip=skip, limit=limit)