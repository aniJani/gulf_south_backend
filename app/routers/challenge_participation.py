from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.crud.user import get_user_by_id, complete_challenge
from app.crud.challenge import get_challenge
from datetime import datetime
from app.crud.challenge_participation import (
    add_participant_to_challenge,
    get_participants_by_challenge,
    get_user_challenges,
)

router = APIRouter()


@router.get("/users/{user_id}/challenges")
def user_challenges(
    user_id: int, completed: bool = None, db: Session = Depends(get_db)
):
    """Get user challenges with optional completion filter"""
    from app.crud.user import (
        get_user_challenges,
    )  # Use the function from user.py instead

    challenges = get_user_challenges(db, user_id, completed)
    return challenges


@router.get("/challenges/{challenge_id}/participants")
def challenge_participants(challenge_id: int, db: Session = Depends(get_db)):
    participants = get_participants_by_challenge(db, challenge_id)
    return participants


@router.post("/challenges/{challenge_id}/participants")
def join_challenge(challenge_id: int, user_id: int, db: Session = Depends(get_db)):
    # Add to ChallengeParticipation table (keeping for compatibility)
    participation = add_participant_to_challenge(db, challenge_id, user_id)

    # Also add to user_challenges association table for completion tracking
    from app.crud.user import join_challenge as add_to_user_challenges

    user = add_to_user_challenges(db, user_id, challenge_id)

    if not participation or not user:
        raise HTTPException(status_code=400, detail="Unable to add participant")

    return {"message": "User added to challenge", "participation": participation}


@router.post("/challenges/{challenge_id}/complete", tags=["Challenge Participation"])
def complete_challenge_endpoint(
    challenge_id: int, user_id: int, db: Session = Depends(get_db)
):
    """Mark a challenge as completed by a user and award points"""
    # Get the user and challenge
    user = get_user_by_id(db, user_id)
    challenge = get_challenge(db, challenge_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")

    # Complete the challenge and award points
    result = complete_challenge(db, user_id, challenge_id)
    if not result:
        raise HTTPException(
            status_code=400,
            detail="Failed to complete challenge. User may not be participating in this challenge.",
        )

    return {
        "message": "Challenge completed successfully",
        "points_earned": challenge.points,
        "total_points": result.total_points,  # Use result.total_points instead of adding points again
    }
