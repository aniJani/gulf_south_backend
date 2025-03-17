from sqlalchemy.orm import Session
from app.models.challenge_participation import ChallengeParticipation


def add_participant_to_challenge(db: Session, challenge_id: int, user_id: int):
    # Checking if the participation already exists
    existing = (
        db.query(ChallengeParticipation)
        .filter_by(challenge_id=challenge_id, user_id=user_id)
        .first()
    )
    if existing:
        return existing
    participation = ChallengeParticipation(challenge_id=challenge_id, user_id=user_id)
    db.add(participation)
    db.commit()
    db.refresh(participation)
    return participation


def get_participants_by_challenge(db: Session, challenge_id: int):
    return db.query(ChallengeParticipation).filter_by(challenge_id=challenge_id).all()


def get_user_challenges(db: Session, user_id: int):
    return db.query(ChallengeParticipation).filter_by(user_id=user_id).all()
