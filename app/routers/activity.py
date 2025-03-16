from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.activity import Activity, ActivityCreate
from app.crud.activity import get_activities, create_activity
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Activity)
def create_activity_endpoint(activity: ActivityCreate, db: Session = Depends(get_db)):
    return create_activity(db, activity)

@router.get("/", response_model=list[Activity])
def read_activities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_activities(db, skip=skip, limit=limit)