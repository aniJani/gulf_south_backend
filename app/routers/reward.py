from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.reward import Reward, RewardCreate
from app.crud.reward import get_rewards, create_reward
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Reward)
def create_reward_endpoint(reward: RewardCreate, db: Session = Depends(get_db)):
    return create_reward(db, reward)

@router.get("/", response_model=list[Reward])
def read_rewards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_rewards(db, skip=skip, limit=limit)