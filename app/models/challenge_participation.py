from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class ChallengeParticipation(Base):
    __tablename__ = "challenge_participation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    challenge_id = Column(Integer, ForeignKey("challenges.id"), nullable=False)
