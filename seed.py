import random
from datetime import datetime, timedelta
from sqlalchemy import text
from app.database import SessionLocal, engine, Base
from app.models.user import User
from app.models.challenge import Challenge
from app.models.team import Team
from app.models.activity import Activity
from app.utils.security import get_password_hash

# --- Create the database if it doesn't exist ---
try:
    from sqlalchemy_utils import database_exists, create_database
except ImportError:
    raise ImportError("Please install sqlalchemy-utils: pip install sqlalchemy-utils")

if not database_exists(engine.url):
    create_database(engine.url)
    print("Database created.")

# --- Create all tables if they don't exist yet ---
Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # --- Create sample users ---
    # Let's create 20 sample users with varying points.
    user_names = [
        "alice",
        "bob",
        "charlie",
        "dave",
        "eve",
        "faythe",
        "grace",
        "heidi",
        "ivan",
        "judy",
        "mallory",
        "oscar",
        "peggy",
        "trent",
        "victor",
        "walter",
        "xander",
        "yvonne",
        "zoe",
        "quentin",
    ]
    users = []
    for name in user_names:
        user = User(
            username=name,
            email=f"{name}@example.com",
            full_name=f"{name.capitalize()} Example",
            hashed_password=get_password_hash("password123"),
            total_points=random.randint(0, 200),  # Random starting points for variety
        )
        db.add(user)
        users.append(user)
    db.commit()
    for user in users:
        db.refresh(user)

    # --- Create sample challenges ---
    # Create 10 challenges with different descriptions and point values.
    challenges = []
    base_titles = [
        "10,000 Steps",
        "Healthy Eating",
        "Yoga Session",
        "Cycling",
        "Meditation",
        "Swimming",
        "Strength Training",
        "Pilates",
        "Dance Class",
        "Hiking Adventure",
    ]
    for i, title in enumerate(base_titles):
        challenge = Challenge(
            title=title,
            description=f"Challenge: {title}. Complete this activity to earn points.",
            points=random.randint(5, 30),
            start_date=datetime.utcnow() - timedelta(days=random.randint(0, 3)),
            end_date=datetime.utcnow() + timedelta(days=7),
            is_active=True,
        )
        db.add(challenge)
        challenges.append(challenge)
    db.commit()
    for challenge in challenges:
        db.refresh(challenge)

    # --- Create sample teams ---
    # Create 5 teams to spread out the users.
    team_names = ["Team Alpha", "Team Bravo", "Team Charlie", "Team Delta", "Team Echo"]
    teams = []
    for name in team_names:
        team = Team(name=name)
        db.add(team)
        teams.append(team)
    db.commit()
    for team in teams:
        db.refresh(team)

    # --- Assign users to teams evenly ---
    # Shuffle users and assign them round-robin to teams.
    random.shuffle(users)
    team_count = len(teams)
    for index, user in enumerate(users):
        team = teams[index % team_count]
        team.users.append(user)
    db.commit()

    # --- Enroll users in challenges and mark some as completed ---
    # For each user, randomly select some challenges to join.
    # For a subset of those challenges, mark them as completed (simulate leaderboard data).
    for user in users:
        selected = random.sample(challenges, k=random.randint(3, len(challenges)))
        for challenge in selected:
            # Enroll the user if not already enrolled
            if challenge not in user.joined_challenges:
                user.joined_challenges.append(challenge)
            # Simulate a 50% chance that the user completed the challenge.
            if random.random() < 0.5:
                # Directly update the association table using raw SQL for simplicity
                # (Assumes the user_challenges table has columns: user_id, challenge_id, completed, completed_at)
                db.execute(
                    text(
                        """
                        UPDATE user_challenges 
                        SET completed = 1, completed_at = :now
                        WHERE user_id = :user_id AND challenge_id = :challenge_id
                        """
                    ),
                    {
                        "now": datetime.utcnow(),
                        "user_id": user.id,
                        "challenge_id": challenge.id,
                    },
                )
                # Award points only if challenge is completed
                user.total_points += challenge.points
        db.commit()

    print("Database seeded successfully with enriched leaderboard data!")
except Exception as e:
    db.rollback()
    print("Error seeding database:", e)
finally:
    db.close()
