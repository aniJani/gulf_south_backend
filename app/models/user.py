from sqlalchemy import Column, Integer, String, DateTime, JSON, Date
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # New columns for weekly challenge selection:
    # Stores a JSON array of challenge IDs selected by the user for the current week.
    weekly_challenge_ids = Column(JSON, nullable=True)
    # Stores the week start date (Sunday) when the challenges were selected.
    weekly_challenge_week = Column(Date, nullable=True)
    
    # Relationship to other tables if needed (e.g., activities, teams, etc.)
    # weekly_challenges are now stored directly in the user row.