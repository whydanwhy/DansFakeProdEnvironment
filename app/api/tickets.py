from fastapi import APIRouter
from app.services.ticket_service import get_all_tickets, create_ticket
from app.schemas.ticket import TicketResponse, TicketCreate
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