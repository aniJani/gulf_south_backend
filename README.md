# Gulf South Wellness Platform

This repository combines two key components of the Gulf South Wellness ecosystem:

1. **Gulf South Wellness Challenge Platform (Backend)**  
   A FastAPI-based backend system designed to engage Gulf South residents in healthier lifestyles through challenges, activities, teams, and more.

2. **Gulf South Wellness (Frontend)**

- Backend: [https://github.com/aniJani/gulf_south_backend](https://github.com/aniJani/gulf_south_backend)
- Frontend: [https://github.com/aniJani/gulf-south-wellness](https://github.com/aniJani/gulf-south-wellness)
---

## Installation & Setup

### Backend: Gulf South Wellness Challenge Platform

#### 1. Clone the Repository

```bash
git clone https://github.com/aniJani/gulf_south_backend
cd gulf_south_backend
```

#### 2. Set Up the Python Environment

You can use either Conda or venv to set up your Python environment:

**Option A: Using Conda**

```bash
conda create --name test1 python=3.10.16
conda activate test1
pip install -r requirements.txt
```

**Option B: Using venv**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
```

#### 3. Create Environment Configuration

Create a `.env` file in the root directory with the following content:

```bash
DATABASE_URL="mysql+pymysql://username:password@localhost/db_name"  # Replace username, password, and db_name with your values
```

For example, your `.env` file might look like this:

```bash
DATABASE_URL="mysql+pymysql://root:YourNewPassword%21@localhost/gulf_south_db"
```

> **Note:** The format of the `DATABASE_URL` is:  
> `"mysql+pymysql://username:password@localhost/db_name"`

#### 4. Database Setup

- **Create a MySQL database** named as specified in your `.env` file (e.g., `gulf_south_db`).
- **Run the seed script** to initialize the database with sample data:

  ```bash
  python seed.py
  ```

  You should see an output like:

  ```
  Database created.
  Database seeded successfully with enriched leaderboard data!
  ```

#### 5. Running the Backend Application

Start the FastAPI server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at:  
`http://localhost:8000`

---

### Frontend: Gulf South Wellness

#### 1. Clone the Repository

```bash
git clone https://github.com/aniJani/gulf-south-wellness.git
cd gulf-south-wellness
```

#### 2. Install Dependencies

```bash
npm install
# or
yarn install
```

#### 3. Configure Environment Variables

Ensure you have a `.env` file in the root directory with the following content:

```bash
VITE_API_BASE_URL=http://localhost:8000  # Use the port where your backend is running
```


#### 4. Running the Frontend Application

Start the development server with:

```bash
npm run dev
# or
yarn dev
```

Once running, access the application at:  
`http://localhost:5173` (or the port specified in your configuration)

---

## Overview

Gulf South Wellness is a comprehensive platform aimed at enhancing the health and wellness of residents in the Gulf South region. The system focuses on challenges, activities, and community engagement to motivate people to pursue activities that enhance health and wellness.

---

## Backend: Gulf South Wellness Challenge Platform

### Features

- **User Management**: Registration, authentication, and profile management
- **Challenges**: Create, join, and complete health and wellness challenges
- **Activities**: Track personal health activities and earn points
- **Teams**: Form teams and collaborate on wellness goals
- **Weekly Challenges**: Select and participate in weekly featured challenges
- **Leaderboards**: View top performers by user, team, and challenge
- **Statistics**: Track individual and challenge participation statistics

### Technology Stack (Backend)

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: Password hashing with Passlib/Bcrypt
- **Environment**: Python 3.10+

---

## API Documentation & Endpoints

When the backend application is running, you can access:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### API Endpoints Overview

**Users**

- `POST /users/`: Create a new user
- `GET /users/`: Get all users
- `POST /users/login`: User login
- `GET /users/{user_id}`: Get user profile
- `PATCH /users/{user_id}`: Update user profile

**Challenges**

- `POST /challenges/`: Create a new challenge
- `GET /challenges/`: Get all challenges
- `POST /challenges/{challenge_id}/participants`: Join a challenge
- `POST /challenges/{challenge_id}/complete`: Complete a challenge

**Activities**

- `POST /activities/`: Create a new activity
- `GET /activities/`: Get all activities
- `GET /activities/user/{user_id}`: Get user's activities
- `PATCH /activities/{activity_id}`: Update an activity
- `POST /activities/{activity_id}/complete`: Complete an activity

**Teams**

- `POST /teams/`: Create a new team
- `GET /teams/`: Get all teams
- `POST /teams/{team_id}/members`: Add a member to a team
- `GET /teams/{team_id}/members`: Get team members

**Leaderboards**

- `GET /leaderboards/users`: Get user leaderboard
- `GET /leaderboards/teams`: Get team leaderboard
- `GET /leaderboards/challenges/{challenge_id}`: Get challenge leaderboard

**Statistics**

- `GET /statistics/user/{user_id}`: Get user statistics
- `GET /statistics/challenge/{challenge_id}`: Get challenge statistics

---

## Project Structure (Backend)

```
gulf_south_backend/
├── app/
│   ├── crud/            # Database operations
│   ├── models/          # SQLAlchemy models
│   ├── routers/         # API routes
│   ├── schemas/         # Pydantic schemas
│   ├── utils/           # Utility functions
│   ├── config.py        # Configuration
│   ├── database.py      # Database connection
│   └── main.py          # Application entry point
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
└── seed.py              # Database seeding script
```

---

## Frontend: Gulf South Wellness

### Technology Stack (Frontend)

- **Frontend Framework**: React.js with Vite build tool
- **API Server**: Connects to the backend (running on port 8000)
- **Database**: MySQL

---

- Backend: [https://github.com/aniJani/gulf_south_backend](https://github.com/aniJani/gulf_south_backend)
- Frontend: [https://github.com/aniJani/gulf-south-wellness](https://github.com/aniJani/gulf-south-wellness)
