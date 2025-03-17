from sqlalchemy.orm import Session
from app.models.user import User, user_challenges
from app.models.challenge import Challenge
from app.schemas.user import UserCreate, UserUpdate
from app.utils.security import get_password_hash
from fastapi import status
from datetime import datetime


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_weekly_challenges(
    db: Session, user_id: int, challenge_ids: list[int], week_start
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.weekly_challenge_ids = challenge_ids
    user.weekly_challenge_week = week_start
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.full_name is not None:
        user.full_name = user_update.full_name
    if user_update.password is not None:
        user.hashed_password = get_password_hash(user_update.password)
    db.commit()
    db.refresh(user)
    return user


def join_challenge(db: Session, user_id: int, challenge_id: int):
    user = get_user_by_id(db, user_id)
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()

    if not user or not challenge:
        return None

    # Check if user already joined the challenge
    if challenge in user.joined_challenges:
        return user

    user.joined_challenges.append(challenge)
    db.commit()
    db.refresh(user)
    return user


def complete_challenge(db: Session, user_id: int, challenge_id: int):
    """Mark a challenge as completed for a user and award points"""
    from sqlalchemy import text

    user = get_user_by_id(db, user_id)
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()

    if not user or not challenge:
        return None

    # Check if user has the challenge in their joined_challenges
    if challenge not in user.joined_challenges:
        return None

    # Transaction management issue - use a single transaction for everything
    with db.begin_nested():  # Use a savepoint for safety
        # Check if already completed using raw SQL
        check_query = text(
            """
            SELECT completed FROM user_challenges 
            WHERE user_id = :user_id AND challenge_id = :challenge_id
        """
        )
        result = db.execute(
            check_query, {"user_id": user_id, "challenge_id": challenge_id}
        )
        record = result.fetchone()

        if record and record[0]:  # Already completed
            return user

        # Update with raw SQL for reliability
        update_query = text(
            """
            UPDATE user_challenges 
            SET completed = 1, completed_at = :now
            WHERE user_id = :user_id AND challenge_id = :challenge_id
        """
        )
        db.execute(
            update_query,
            {
                "now": datetime.utcnow(),
                "user_id": user_id,
                "challenge_id": challenge_id,
            },
        )

        # Award points to user
        user.total_points += challenge.points

    # Commit the entire transaction
    db.commit()

    # Refresh to ensure we have the latest data
    db.refresh(user)
    return user


def get_user_challenges(db: Session, user_id: int, completed: bool = None):
    """Get user's challenges with optional completion filter"""
    user = get_user_by_id(db, user_id)
    if not user:
        return []

    # Always use a join query to get completion information
    query = (
        db.query(Challenge, user_challenges.c.completed, user_challenges.c.completed_at)
        .join(user_challenges, Challenge.id == user_challenges.c.challenge_id)
        .filter(user_challenges.c.user_id == user_id)
    )

    # Only apply completion filter if explicitly requested
    if completed is not None:
        query = query.filter(user_challenges.c.completed == completed)

    results = query.all()

    # Create serializable dictionaries with completion data
    return [
        {
            "id": row[0].id,
            "title": row[0].title,
            "description": row[0].description,
            "points": row[0].points,
            "start_date": row[0].start_date,
            "end_date": row[0].end_date,
            "is_active": row[0].is_active,
            "created_at": row[0].created_at,
            "completed": row[1],
            "completed_at": row[2],
        }
        for row in results
    ]
