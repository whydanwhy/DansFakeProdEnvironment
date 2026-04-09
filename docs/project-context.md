# Project Context — Ticket API

## Overview

A full-stack ticket management system built with FastAPI, SQLite, and a simple HTML/JS frontend.

## Architecture

* Backend: FastAPI
* Database: SQLite
* Frontend: Vanilla HTML + JavaScript
* Deployment: Render
* Containerization: Docker
* CI: GitHub Actions

## Current Features

* Create ticket (POST /tickets/)
* Get tickets (GET /tickets/)
* Update ticket (PUT /tickets/{id})
* Close ticket (PATCH /tickets/{id}/close)
* Status tracking (open/closed)
* Basic frontend dashboard
* Ticket detail page (in progress)

## Data Model (Current)

Ticket:

* id
* title
* description
* status

## Current Focus

Building ticket detail page and preparing for notes system.

## Next Steps

* Add notes (1-to-many relationship)
* Add ticket detail API endpoint
* Improve frontend UX

## Known Limitations

* SQLite not persistent in deployment
* No authentication
* No validation for duplicate tickets

## How to Run

* Local: uvicorn app.main:app --reload
* Docker: docker run -p 8000:8000 ticket-api

## Notes for Contributors / AI

* Follow existing service layer pattern
* Keep API RESTful
* Maintain structured logging
* Update schemas when changing response models

