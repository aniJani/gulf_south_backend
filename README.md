# Gulf South Wellness Platform

This is the backend repository for an ecosystem that combines two key components of the Gulf South Wellness ecosystem:

1. **Gulf South Wellness Challenge Platform (Backend)**  
   A FastAPI-based backend system designed to engage Gulf South residents in healthier lifestyles through challenges, activities, teams, and more.

2. **Gulf South Wellness (Frontend)**  
   A Vue.js-based frontend application that provides an intuitive interface for users to engage with the wellness platform.

- Backend: [https://github.com/aniJani/gulf_south_backend](https://github.com/aniJani/gulf_south_backend)
- Frontend: [https://github.com/aniJani/gulf-south-wellness](https://github.com/aniJani/gulf-south-wellness)
---
## Video Demonstration

Watch our platform demonstration to see the project in action:

[![Gulf South Wellness Platform Demo](https://img.youtube.com/vi/i6BroYUmjYw/0.jpg)](https://www.youtube.com/watch?v=i6BroYUmjYw)

*Click the image above to watch the demo video*
## Installation & Setup

### Backend: Gulf South Wellness Challenge Platform

#### 1. Clone the Repository

```bash
git clone https://github.com/aniJani/gulf_south_backend
cd gulf_south_backend
```

#### 2. Set Up the Python Environment

You can use Conda to set up your environment:
Replace test1 with what you want your environment name to be.

```bash
conda create --name test1 python=3.10.16 
conda activate test1
pip install -r requirements.txt
```

#### 3. Database Prerequisites

**Important:** Before proceeding, ensure you have MySQL server installed and running on your system. You'll need to have:
- MySQL server installed and running
- Admin access or a user with privileges to create databases
- Your MySQL username and password readily available

#### 4. Create Environment Configuration

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

#### 5. Database Setup

- **seed.py** automatically creates a database named as specified in your `.env` file (e.g., `gulf_south_db`).
- **If you already have a database** and you want to use that database first make sure it is empty and use the same name in your `.env` file (e.g., `gulf_south_db`).
- **Run the seed script** to initialize the database with sample data:

  ```bash
  python seed.py
  ```

  You should see an output like:

  ```
  Database created. #you will not see this if you have a already created database in your .env. This does not indicate an error.
  Database seeded successfully with enriched leaderboard data!
  ```

#### 6. Running the Backend Application

Start the FastAPI server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at port 8000, if not change the port number in the frontend accordingly.:  
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
```

Once running, access the application at:  
`http://localhost:5173` (or the port specified in your configuration)

---

## Overview

Gulf South Wellness is a comprehensive platform aimed at enhancing the health and wellness of people who are motivated by a more collaborative environment. The system focuses on challenges, activities, and community engagement to motivate people to pursue activities that enhance health and wellness.

---

## Backend: Gulf South Wellness Challenge Platform

### Features

- **User Management**: Registration, authentication, and profile management
- **Challenges**: Create, join, and complete health and wellness challenges
- **Activities**: Track personal health activities and earn points
- **Teams**: Form teams and collaborate on wellness goals
- **Leaderboards**: View top performers by user, and teams.
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
- `DELETE /activities/{activity_id}`: DELETE an incomplete activity
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

### Features

- **User Authentication**: Login/signup functionality with secure token-based sessions
- **Dashboard**: Overview of user's wellness journey with statistics and charts
- **Challenges**: Browse, join, and complete wellness challenges
- **Activities**: Create, track, and complete personal wellness activities
- **Teams**: Create or join teams to collaborate on wellness goals
- **Profile**: View and update user profile and activity history
- **Leaderboards**: View top performers by user and team rankings
- **Theme Toggle**: Light and dark mode support with persistent user preference

### Technology Stack (Frontend)

- **Framework**: Vue 3 with Composition API
- **Build Tool**: Vite
- **State Management**: Pinia
- **Routing**: Vue Router
- **HTTP Client**: Axios
- **Data Visualization**: Chart.js
- **Styling**: Custom CSS with CSS variables for theming

### Project Structure (Frontend)

```
gulf-south-wellness/
├── public/                   # Static assets
├── src/
│   ├── components/           # Reusable UI components
│   │   ├── layout/           # Layout components (Sidebar, Auth/MainLayout)
│   │   └── ui/               # UI components (ActivityChart, ChallengeCard)
│   ├── services/             # API service layer
│   │   └── api.js            # API endpoints and Axios config
│   ├── store/                # Pinia state management
│   │   └── auth.js           # Authentication state
│   ├── utils/                # Utility functions
│   │   └── theme.js          # Theme initialization and management
│   ├── views/                # Page components
│   │   ├── Auth.vue          # Authentication page
│   │   ├── Challenges.vue    # Challenges and activities page
│   │   ├── Dashboard.vue     # Main dashboard page
│   │   ├── Profile.vue       # User profile page
│   │   └── Teams.vue         # Teams management page
│   ├── App.vue               # Root component
│   ├── main.js               # Application entry point
│   ├── router/               # Vue router configuration
│   └── style.css             # Global styles and CSS variables
├── .env                      # Environment variables
├── index.html                # HTML entry point
├── package.json              # Dependencies and scripts
└── vite.config.js            # Vite configuration
```

### Key Components

- **Layouts**: MainLayout.vue, AuthLayout.vue, Sidebar.vue
- **Pages**: Dashboard.vue, Challenges.vue, Teams.vue, Profile.vue, Auth.vue
- **UI Components**: ActivityChart.vue, ChallengeCard.vue
- **State Management**: Authentication with Pinia store


### API Integration

- Centralized API service using Axios
- Endpoints for users, challenges, activities, teams, and statistics
- Auth state management with local storage

---

- Backend: [https://github.com/aniJani/gulf_south_backend](https://github.com/aniJani/gulf_south_backend)
- Frontend: [https://github.com/aniJani/gulf-south-wellness](https://github.com/aniJani/gulf-south-wellness)
