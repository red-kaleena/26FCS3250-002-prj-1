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

## Team Evaluation

> Important: every member must submit the team/self-evaluation form —
> the team grade is held until all evaluations are in.