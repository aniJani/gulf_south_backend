from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.utils.security import verify_password
from app.crud.user import (
    get_user_by_email,
    get_user_by_username,
    create_user,
    get_users,
)
from app.database import get_db

router = APIRouter()
# Create a new user


@router.post("/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, email=user.email) or get_user_by_username(
        db, username=user.username
    ):
        raise HTTPException(
            status_code=400, detail="User with given email or username already exists"
        )
    return create_user(db, user)


# Get all users
@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)


# Login
@router.post("/login", response_model=User)
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    return user
