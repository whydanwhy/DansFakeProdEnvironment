"""
Ticket API routes.

Handles HTTP requests related to ticket operations,
including creating and retrieving tickets.
"""
from fastapi import APIRouter, HTTPException, status
from app.services.ticket_service import (
    get_all_tickets,
    create_ticket,
    update_ticket,
    close_ticket,
    get_ticket_by_id
)
from app.schemas.ticket import (
    TicketResponse,
    TicketCreate,
    TicketUpdate,
    TicketDetail
)
from app.core.logger import logger

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("/", response_model=TicketResponse, status_code=status.HTTP_200_OK)
def fetch_tickets():
    logger.info("GET /tickets called")
    return get_all_tickets()


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_ticket(ticket: TicketCreate):
    logger.info(f"POST /tickets called | title={ticket.title}")
    return create_ticket(ticket.title, ticket.description)


@router.put("/{ticket_id}", status_code=status.HTTP_200_OK)
def update_ticket_endpoint(ticket_id: int, ticket: TicketUpdate):
    updated = update_ticket(ticket_id, ticket.title, ticket.description)

    if not updated:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return updated


@router.patch("/{ticket_id}/close", status_code=status.HTTP_200_OK)
def close_ticket_endpoint(ticket_id: int):
    closed = close_ticket(ticket_id)

    if not closed:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return closed


@router.get("/{ticket_id}", response_model=TicketDetail, status_code=status.HTTP_200_OK)
def fetch_ticket(ticket_id: int):
    logger.info(f"GET /tickets/{ticket_id} called")

    ticket = get_ticket_by_id(ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {
        "id": ticket[0],
        "title": ticket[1],
        "description": ticket[2],
        "status": ticket[3]
    }