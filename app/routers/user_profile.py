from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import User, UserUpdate
from app.crud.user import get_user_by_id, update_user
from app.database import get_db

router = APIRouter()


@router.get("/{user_id}", response_model=User)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/{user_id}", response_model=User)
def patch_user_profile(
    user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)
):
    updated_user = update_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
