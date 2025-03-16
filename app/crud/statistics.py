from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.activity import Activity
from app.models.challenge_participation import ChallengeParticipation
from app.models.reward import Reward


def get_user_statistics(db: Session, user_id: int):
    activities_count = (
        db.query(func.count(Activity.id)).filter(Activity.user_id == user_id).scalar()
    )
    challenges_count = (
        db.query(func.count(ChallengeParticipation.id))
        .filter(ChallengeParticipation.user_id == user_id)
        .scalar()
    )
    total_points = (
        db.query(func.coalesce(func.sum(Reward.points), 0))
        .filter(Reward.user_id == user_id)
        .scalar()
    )
    return {
        "user_id": user_id,
        "activities_count": activities_count,
        "challenges_joined": challenges_count,
        "total_points": total_points,
    }


def get_challenge_statistics(db: Session, challenge_id: int):
    participants_count = (
        db.query(func.count(ChallengeParticipation.id))
        .filter(ChallengeParticipation.challenge_id == challenge_id)
        .scalar()
    )
    activities_count = (
        db.query(func.count(Activity.id))
        .filter(Activity.challenge_id == challenge_id)
        .scalar()
    )
    avg_activities = 0
    if participants_count > 0:
        avg_activities = activities_count / participants_count
    return {
        "challenge_id": challenge_id,
        "participants_count": participants_count,
        "activities_count": activities_count,
        "avg_activities_per_participant": avg_activities,
    }
