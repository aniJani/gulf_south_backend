from sqlalchemy.orm import Session
from app.models.challenge import Challenge
from app.schemas.challenge import ChallengeCreate, ChallengeUpdate
import random


def get_challenge(db: Session, challenge_id: int):
    """Get a challenge by its ID"""
    return db.query(Challenge).filter(Challenge.id == challenge_id).first()


def get_challenge_by_title(db: Session, title: str):
    return db.query(Challenge).filter(Challenge.title == title).first()


def get_challenges(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Challenge).offset(skip).limit(limit).all()


def get_weekly_challenge_options(db: Session):
    # Return exactly 7 random challenges from the entire pool
    all_challenges = db.query(Challenge).all()
    if len(all_challenges) <= 7:
        return all_challenges
    return random.sample(all_challenges, 7)


def create_challenge(db: Session, challenge: ChallengeCreate):
    db_challenge = Challenge(
        title=challenge.title,
        description=challenge.description,
        points=challenge.points,  # Add points field
        start_date=challenge.start_date,
        end_date=challenge.end_date,
        is_active=challenge.is_active,
    )
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge


def update_challenge(db: Session, challenge_id: int, challenge: ChallengeUpdate):
    db_challenge = get_challenge(db, challenge_id)
    if not db_challenge:
        return None

    # Update fields that are provided
    update_data = challenge.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_challenge, key, value)

    db.commit()
    db.refresh(db_challenge)
    return db_challenge
