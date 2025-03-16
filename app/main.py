from fastapi import FastAPI
from app.database import engine, Base

# Explicitly import all models to register with Base
from app.models.challenge import Challenge
from app.models.user import User
from app.models.activity import Activity
from app.models.team import Team, user_teams
from app.models.reward import Reward

# Create tables in the database if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gulf South Wellness Challenge Platform",
    description="An engaging platform to encourage healthier lifestyles for Gulf South residents.",
    version="0.1.0",
)

# Explicitly import all routers
from app.routers.challenge import router as challenge
from app.routers.user import router as user
from app.routers.activity import router as activity
from app.routers.team import router as team
from app.routers.reward import router as reward
from app.routers.weekly_challenges import router as weekly_challenges

app.include_router(challenge, prefix="/challenges", tags=["Challenges"])
app.include_router(user, prefix="/users", tags=["Users"])
app.include_router(activity, prefix="/activities", tags=["Activities"])
app.include_router(team, prefix="/teams", tags=["Teams"])
app.include_router(reward, prefix="/rewards", tags=["Rewards"])
app.include_router(
    weekly_challenges, prefix="/weekly-challenges", tags=["Weekly Challenges"]
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Gulf South Wellness Challenge Platform"}
