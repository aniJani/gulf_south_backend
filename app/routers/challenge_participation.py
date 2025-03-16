from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.challenge_participation import (
    add_participant_to_challenge,
    get_participants_by_challenge,
    get_user_challenges,
)

router = APIRouter()


@router.get("/users/{user_id}/challenges")
def user_challenges(user_id: int, db: Session = Depends(get_db)):
    challenges = get_user_challenges(db, user_id)
    return challenges


@router.get("/challenges/{challenge_id}/participants")
def challenge_participants(challenge_id: int, db: Session = Depends(get_db)):
    participants = get_participants_by_challenge(db, challenge_id)
    return participants


@router.post("/challenges/{challenge_id}/participants")
def join_challenge(challenge_id: int, user_id: int, db: Session = Depends(get_db)):
    participation = add_participant_to_challenge(db, challenge_id, user_id)
    if not participation:
        raise HTTPException(status_code=400, detail="Unable to add participant")
    return {"message": "User added to challenge", "participation": participation}
