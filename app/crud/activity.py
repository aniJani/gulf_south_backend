from sqlalchemy.orm import Session
from app.models.activity import Activity
from app.models.user import User
from app.schemas.activity import ActivityCreate, ActivityUpdate
from datetime import datetime


def get_activities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Activity).offset(skip).limit(limit).all()


def create_activity(db: Session, activity: ActivityCreate, user_id: int):
    db_activity = Activity(
        title=activity.title,
        description=activity.description,
        points=activity.points,
        user_id=user_id,
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_user_activities(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(Activity)
        .filter(Activity.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_activity(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()


def update_activity(db: Session, activity_id: int, activity: ActivityUpdate):
    db_activity = get_activity(db, activity_id)
    if not db_activity:
        return None

    for key, value in activity.dict(exclude_unset=True).items():
        setattr(db_activity, key, value)

    db.commit()
    db.refresh(db_activity)
    return db_activity


def complete_activity(db: Session, activity_id: int, user_id: int):
    db_activity = get_activity(db, activity_id)
    if not db_activity or db_activity.user_id != user_id:
        return None

    # Check if already completed
    if db_activity.is_completed:
        return db_activity

    # Mark as completed and award points
    db_activity.is_completed = True
    db_activity.completed_at = datetime.utcnow()

    # Update user points
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.total_points += db_activity.points

    db.commit()
    db.refresh(db_activity)
    return db_activity


def delete_activity(db: Session, activity_id: int):
    db_activity = get_activity(db, activity_id)
    if not db_activity:
        return False

    db.delete(db_activity)
    db.commit()
    return True
