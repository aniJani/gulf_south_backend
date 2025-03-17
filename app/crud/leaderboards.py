from sqlalchemy.orm import Session
from sqlalchemy import func
from app.crud.challenge_participation import get_participants_by_challenge
from app.models.team import Team
from app.models.user import User


def get_challenge_leaderboard(db: Session, challenge_id: int):
    # Get participants who completed the challenge with their points
    result = db.execute(
        """
        SELECT u.id, u.username, u.total_points 
        FROM users u
        JOIN user_challenges uc ON u.id = uc.user_id
        WHERE uc.challenge_id = :challenge_id AND uc.completed = true
        ORDER BY u.total_points DESC
        """,
        {"challenge_id": challenge_id},
    )

    participants = [
        {"user_id": row[0], "username": row[1], "points": row[2]}
        for row in result.fetchall()
    ]

    return {
        "challenge_id": challenge_id,
        "participants": participants,
        "participant_count": len(participants),
    }


def get_team_leaderboard(db: Session):
    # Get teams with the sum of their members' points
    teams = db.query(Team).all()
    leaderboard = []

    for team in teams:
        total_points = sum(user.total_points for user in team.users)
        leaderboard.append(
            {
                "team_id": team.id,
                "team_name": team.name,
                "points": total_points,
                "member_count": len(team.users),
            }
        )

    # Sort by points in descending order
    leaderboard.sort(key=lambda x: x["points"], reverse=True)
    return leaderboard


def get_user_leaderboard(db: Session, limit: int = 10):
    # Get top users by points
    top_users = (
        db.query(User.id, User.username, User.total_points)
        .order_by(User.total_points.desc())
        .limit(limit)
        .all()
    )

    return [
        {"user_id": user.id, "username": user.username, "points": user.total_points}
        for user in top_users
    ]
