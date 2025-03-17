from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.activity import Activity
from app.models.user import User, user_challenges
from app.models.challenge import Challenge


def get_user_statistics(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    activities_count = (
        db.query(func.count(Activity.id)).filter(Activity.user_id == user_id).scalar()
    )

    activities_completed = (
        db.query(func.count(Activity.id))
        .filter(Activity.user_id == user_id, Activity.is_completed == True)
        .scalar()
    )

    challenges_count = (
        db.query(func.count(user_challenges.c.challenge_id))
        .filter(user_challenges.c.user_id == user_id)
        .scalar()
    )

    challenges_completed = (
        db.query(func.count(user_challenges.c.challenge_id))
        .filter(
            user_challenges.c.user_id == user_id, user_challenges.c.completed == True
        )
        .scalar()
    )

    return {
        "user_id": user_id,
        "username": user.username,
        "total_points": user.total_points,
        "activities_count": activities_count,
        "activities_completed": activities_completed,
        "challenges_joined": challenges_count,
        "challenges_completed": challenges_completed,
    }


def get_challenge_statistics(db: Session, challenge_id: int):
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()
    if not challenge:
        return None

    participants_count = (
        db.query(func.count(user_challenges.c.user_id))
        .filter(user_challenges.c.challenge_id == challenge_id)
        .scalar()
    )

    completions_count = (
        db.query(func.count(user_challenges.c.user_id))
        .filter(
            user_challenges.c.challenge_id == challenge_id,
            user_challenges.c.completed == True,
        )
        .scalar()
    )

    completion_rate = 0
    if participants_count > 0:
        completion_rate = (completions_count / participants_count) * 100

    return {
        "challenge_id": challenge_id,
        "title": challenge.title,
        "points_value": challenge.points,
        "participants_count": participants_count,
        "completions_count": completions_count,
        "completion_rate": completion_rate,
    }
