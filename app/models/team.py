from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

user_teams = Table(
    "user_teams",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("team_id", Integer, ForeignKey("teams.id"), primary_key=True),
)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship("User", secondary=user_teams, backref="teams")
