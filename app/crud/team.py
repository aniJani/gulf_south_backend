from sqlalchemy.orm import Session
from app.models.team import Team
from app.schemas.team import TeamCreate
from app.models.user import User


def get_team_by_name(db: Session, name: str):
    return db.query(Team).filter(Team.name == name).first()


def get_teams(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Team).offset(skip).limit(limit).all()


def create_team(db: Session, team: TeamCreate):
    db_team = Team(name=team.name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def add_member_to_team(db: Session, team_id: int, user_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        return None
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    if user not in team.users:
        team.users.append(user)
    db.commit()
    db.refresh(team)
    return team


def get_team_members(db: Session, team_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    if team:
        return team.users
    return []
