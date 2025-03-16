from sqlalchemy.orm import Session
from app.models.challenge import Challenge
from app.schemas.challenge import ChallengeCreate
import random

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
        end_date=challenge.end_date,
    )
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge