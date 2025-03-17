from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.activity import Activity, ActivityCreate, ActivityUpdate
from app.crud.activity import (
    get_activities,
    create_activity,
    get_user_activities,
    get_activity,
    update_activity,
    complete_activity,
    delete_activity,
)
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=Activity)
def create_activity_endpoint(
    activity: ActivityCreate, user_id: int, db: Session = Depends(get_db)
):
    return create_activity(db, activity, user_id)


@router.get("/", response_model=list[Activity])
def read_activities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_activities(db, skip=skip, limit=limit)


@router.get("/user/{user_id}", response_model=list[Activity])
def get_activities_by_user(
    user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return get_user_activities(db, user_id, skip=skip, limit=limit)


@router.get("/{activity_id}", response_model=Activity)
def get_activity_endpoint(activity_id: int, db: Session = Depends(get_db)):
    activity = get_activity(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@router.patch("/{activity_id}", response_model=Activity)
def update_activity_endpoint(
    activity_id: int, activity_update: ActivityUpdate, db: Session = Depends(get_db)
):
    updated_activity = update_activity(db, activity_id, activity_update)
    if not updated_activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return updated_activity


@router.post("/{activity_id}/complete", response_model=Activity)
def complete_activity_endpoint(
    activity_id: int, user_id: int, db: Session = Depends(get_db)
):
    completed_activity = complete_activity(db, activity_id, user_id)
    if not completed_activity:
        raise HTTPException(
            status_code=404, detail="Activity not found or not authorized"
        )
    return completed_activity


@router.delete("/{activity_id}")
def delete_activity_endpoint(
    activity_id: int, user_id: int, db: Session = Depends(get_db)
):
    """Delete an activity, but only if incomplete and owned by the user"""
    result = delete_activity(db, activity_id, user_id)

    if not result["success"]:
        if result["reason"] == "not_found":
            raise HTTPException(status_code=404, detail="Activity not found")
        elif result["reason"] == "not_owner":
            raise HTTPException(
                status_code=403, detail="You can only delete your own activities"
            )
        elif result["reason"] == "already_completed":
            raise HTTPException(
                status_code=400, detail="Cannot delete completed activities"
            )

    return {"message": "Activity deleted successfully"}
