from sqlalchemy.orm import Session
from app.models.reward import Reward
from app.schemas.reward import RewardCreate

def get_rewards(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reward).offset(skip).limit(limit).all()

def create_reward(db: Session, reward: RewardCreate):
    db_reward = Reward(
        reward_type=reward.reward_type,
        description=reward.description,
        points=reward.points,
        user_id=reward.user_id
    )
    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)
    return db_reward