from sqlalchemy.orm import Session
from app.crud.challenge_participation import get_participants_by_challenge
from app.models.team import Team


def get_challenge_leaderboard(db: Session, challenge_id: int):
    # For demonstration, return participant count
    participants = get_participants_by_challenge(db, challenge_id)
    leaderboard = {"challenge_id": challenge_id, "participant_count": len(participants)}
    return leaderboard


def get_team_leaderboard(db: Session):
    # Dummy implementation: return list of teams with placeholder points
    teams = db.query(Team).all()
    leaderboard = [
        {"team_id": team.id, "team_name": team.name, "points": 0} for team in teams
    ]
    return leaderboard
