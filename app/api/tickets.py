"""
Ticket API routes.

Handles HTTP requests related to ticket operations,
Including creating a retrieving tickets.
"""
from fastapi import APIRouter
from fastapi import HTTPException
from app.services.ticket_service import get_all_tickets, create_ticket, update_ticket, close_ticket, get_ticket_by_id
from app.schemas.ticket import TicketResponse, TicketCreate, TicketUpdate
from app.core.logger import logger

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("/", response_model=TicketResponse)
def fetch_tickets():
    logger.info("GET /tickets called")
    return get_all_tickets()


@router.post("/")
def add_ticket(ticket: TicketCreate):
    logger.info(f"POST /tickets called | title={ticket.title}")
    return create_ticket(ticket.title, ticket.description)

@router.put("/{ticket_id}")
def update_ticket_endpoint(ticket_id:int, ticket: TicketUpdate):
    return update_ticket(ticket_id, ticket.title, ticket.description)

@router.patch("/{ticket_id}/close")
def close_ticket_endpoint(ticket_id: int):
    return close_ticket(ticket_id)

@router.get("/{ticket_id}")
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
