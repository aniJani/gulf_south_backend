from fastapi import FastAPI
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Import all models (including new ones)
from app.models.challenge import Challenge
from app.models.user import User
from app.models.activity import Activity
from app.models.team import Team, user_teams
from app.models.reward import Reward
from app.models.challenge_participation import ChallengeParticipation  # New model

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Gulf South Wellness Challenge Platform",
    description="An engaging platform to encourage healthier lifestyles for Gulf South residents.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Import routers
from app.routers import (
    challenge,
    user,
    activity,
    team,
    reward,
    weekly_challenges,
    user_profile,
    challenge_participation,
    leaderboards,
    statistics,
)

app.include_router(challenge.router, prefix="/challenges", tags=["Challenges"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(activity.router, prefix="/activities", tags=["Activities"])
app.include_router(team.router, prefix="/teams", tags=["Teams"])
app.include_router(reward.router, prefix="/rewards", tags=["Rewards"])
app.include_router(
    weekly_challenges.router, prefix="/weekly-challenges", tags=["Weekly Challenges"]
)

# New endpoints
app.include_router(user_profile.router, prefix="/users", tags=["User Profile"])
app.include_router(challenge_participation.router, tags=["Challenge Participation"])
app.include_router(leaderboards.router, tags=["Leaderboards"])
app.include_router(statistics.router, tags=["Statistics"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Gulf South Wellness Challenge Platform"}
