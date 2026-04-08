"""
App entry point.

Initialises the FASTAPI application, sets up logging, middle ware and registers API routes.
"""
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api import tickets
from app.db.database import init_db
from app.core.logger import logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

logger.info("Starting application")

init_db()

app.include_router(tickets.router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(
        "request completed",
        extra={
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration": round(duration, 4),
        }
    )

    return response