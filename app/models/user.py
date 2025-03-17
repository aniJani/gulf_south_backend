from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# User-Challenge association table
user_challenges = Table(
    "user_challenges",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("challenge_id", Integer, ForeignKey("challenges.id"), primary_key=True),
    Column("joined_at", DateTime, default=datetime.utcnow),
    Column("completed", Boolean, default=False),
    Column("completed_at", DateTime, nullable=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    total_points = Column(Integer, default=0)
    weekly_challenge_ids = Column(String(255), nullable=True)
    weekly_challenge_week = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    joined_challenges = relationship(
        "Challenge", secondary=user_challenges, back_populates="participants"
    )
    activities = relationship("Activity", back_populates="user")
