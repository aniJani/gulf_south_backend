from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.crud.user import update_user_weekly_challenges
from app.database import get_db

router = APIRouter()


# Get the start of the current week
def get_current_week_start() -> date:
    today = date.today()
    days_since_sunday = (today.weekday() + 1) % 7
    return today - timedelta(days=days_since_sunday)


# Get the weekly challenges for the current week
@router.get("/", response_model=dict)
def get_weekly_challenges(user_id: int, db: Session = Depends(get_db)):
    from app.models.user import User

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    week_start = get_current_week_start()
    if user.weekly_challenge_week != week_start or not user.weekly_challenge_ids:
        return {
            "selected_challenges": None,
            "message": "No weekly challenges selected for the current week.",
        }
    return {
        "selected_challenges": user.weekly_challenge_ids,
        "week_start": str(user.weekly_challenge_week),
    }


# Select the weekly challenges for the current week
@router.post("/", response_model=dict)
def select_weekly_challenges(
    user_id: int, challenge_ids: list[int], db: Session = Depends(get_db)
):
    if len(challenge_ids) != 3:
        raise HTTPException(
            status_code=400, detail="You must select exactly 3 challenges."
        )
    week_start = get_current_week_start()
    user = update_user_weekly_challenges(db, user_id, challenge_ids, week_start)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "message": "Weekly challenges updated.",
        "selected_challenges": user.weekly_challenge_ids,
        "week_start": str(user.weekly_challenge_week),
    }
