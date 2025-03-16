from sqlalchemy.orm import Session
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate

def get_activities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Activity).offset(skip).limit(limit).all()

def create_activity(db: Session, activity: ActivityCreate):
    db_activity = Activity(
        description=activity.description,
        user_id=activity.user_id,
        challenge_id=activity.challenge_id
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity