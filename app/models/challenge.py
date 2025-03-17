from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(Text)
    points = Column(Integer, default=0)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    participants = relationship(
        "User", secondary="user_challenges", back_populates="joined_challenges"
    )
