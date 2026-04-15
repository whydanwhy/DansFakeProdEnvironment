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
    get_ticket_by_id,
    add_note,
    get_ticket_with_notes
)
from app.schemas.ticket import (
    TicketResponse,
    TicketCreate,
    TicketUpdate,
    TicketDetail,
    NoteCreate
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


@router.post("/{ticket_id}/notes", status_code=status.HTTP_200_OK)
def create_note(ticket_id: int, note: NoteCreate):
    print("NOTE RECEIVED:", note)
    note_updated=add_note(ticket_id, note.content)

    if not note_updated:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    return note_updated


@router.get("/{ticket_id}", status_code=status.HTTP_200_OK)
def get_ticket(ticket_id: int):
    print(">>> USING NEW ENDPOINT <<<")
    ticket = get_ticket_with_notes(ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    return ticket


