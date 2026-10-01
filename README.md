# GPA Calculator Web App

> CS3250 - Software Development Methods and Tools (Project 1)
> A simple web application that lets students track their GPA.

![Status](https://img.shields.io/badge/status-in_development-orange)
![CI](https://img.shields.io/badge/CI-not_configured-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)

## Overview

Students register, log in, add the courses they completed together with their
letter grades, and instantly see their credit-weighted GPA. Every grade can be
updated or a course deleted. The app is a proof of concept built on a
Flask + SQLAlchemy baseline.

## Branch Model

```
feature/* ──PR──▶ dev ──PR──▶ main ──tag──▶ PyPI + Docker
```

- `main` — stable, protected, only via PR from `dev`.
- `dev` — integration branch for all feature work.
- `feature/*` — short-lived branches per task, created from `dev`.

## Schedule

| Phase | Task | Start | End | Duration | Deliverable |
|---|---|---|---|---|---|
| Modeling | Requirements Analysis | 09/16/26 | 09/17/26 | 2 days | Use Case Diagram |
| Modeling | Data Model | 09/17/26 | 09/18/26 | 2 days | Class Diagram |
| Construction | Coding | 09/18/26 | 10/01/26 | 14 days | Code |
| Construction | Testing | 10/02/26 | 10/05/26 | 4 days | Test Report |
| Deployment | Delivery | 10/06/26 | 10/07/26 | 2 days | Final Commit/Push |

## Team Roles

| Name | Role(s) |
|---|---|
| Hlib Yeromin | manager (owner) |
| Richard Hall | developer |
| Riley Drenth | testing and documentation |

## Manual Testing Log

| Functionality Tested | Date | Time | Result |
|---|---|---|---|
| Sign Up | 10/01/26 | 14:30 | passed |
| Login / Signout | 10/01/26 | 14:30 | passed |
| List Enrollments | 10/01/26 | 14:31 | passed |
| Create Enrollment | 10/01/26 | 14:31 | passed |
| Delete Enrollment | 10/01/26 | 14:32 | passed |
| Update Grade / GPA | 10/01/26 | 14:32 | passed |

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Framework | [Flask](https://flask.palletsprojects.com/) | Web application framework |
| ORM | [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) | Database ORM for models (`User`, `Course`, `Enrollment`) |
| Forms | [Flask-WTF](https://flask-wtf.readthedocs.io/) / [WTForms](https://wtforms.readthedocs.io/) | Form handling and CSRF protection |
| Auth | [Flask-Login](https://flask-login.readthedocs.io/) | User session management |
| Hashing | [bcrypt](https://pypi.org/project/bcrypt/) | Secure password hashing |
| Database | [SQLite](https://www.sqlite.org/) | Local development database (`instance/prj1.db`) |
| GPA Library | [gpa_calculator](./src/gpa_calculator) | Credit-weighted GPA calculation module |
| Packaging | [hatchling](https://hatch.pypa.io/) | Build backend for PyPI distribution |

## Getting Started

### Prerequisites

- Python 3.9+
- macOS/Linux/Windows

### Installation

```bash
# Clone the repository
cd "project 1"

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Navigate to source directory
cd src

# Set Flask environment variable
export FLASK_APP=app  # On Windows (CMD): set FLASK_APP=app
                      # On Windows (PowerShell): $env:FLASK_APP="app"

# Run the application
flask run --host 127.0.0.1 --port 5000
```

Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

1. **Sign Up** - Create a new account with ID, name, password, and confirmation
2. **Log In** - Authenticate with your credentials
3. **Grade Entry** - Click "Grade Entry" to add a course with its letter grade
4. **View Enrollments** - See all enrolled courses with credits, grades, and calculated GPA
5. **Delete Enrollment** - Remove a course (GPA automatically recalculates)
6. **Sign Out** - End your session

## UML Diagrams

### Use Case Diagram

![Use Case Diagram](pics/pic1.png)

### Class Diagram

![Class Diagram](pics/pic3.png)

## Team Evaluation

> Important: every member must submit the team/self-evaluation form —
> the team grade is held until all evaluations are in.