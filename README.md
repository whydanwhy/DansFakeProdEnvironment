Dans Fake Prod Environment

SUMMARY
This project is a backend ticketing system built using FASTAPI.
It simulates a production style service with structured architectured, logging, and database persistence.

The Goal of this product is to develop a real world backend engineering skills, including API design, observability and a system structure.

I'm trying to move from Application support to Site realibility engineer or Support engineer, so as I complete more complex environment I will use this system to:
A) Build a first project from start to finish.
B) Be able to log and demonstrate my troubleshooting skills and provide evidence of my abilities.
C) Use ticket logging to reenforce learning to ensure I deeply understand the applications I build and tools I learn.


FEATURES

- Create tickets via API (POST /tickets)
- Retrieve tickets via API ( GET /tickets)
- Update tickets via API (PUT /tickets)
- Close tickets via API (PATCH /tickets)
- SQLite database persistence
- Layered architecture ( Api to Service to DB )
- Request logging midle ware (and eventually automated ticket creation)
- Structured application logging (and eventually SQL log analysis and a front end to display)

TECH STACK

- Python
- FastAPI
- SQLite
- Uvicorn
- Lots of coffee

Project Structure

app/
- api/		# API
- services/ 	# Business Logic
- db/		# Database connection and setup
- schemas/	# Request and response models
- core/		# Logging and configuration
- main.py	# Application entry point
