from pydantic import BaseModel
from typing import List


class Ticket(BaseModel):
    id: int
    title: str
    status: str


class TicketCreate(BaseModel):
    title: str
    description: str


class TicketResponse(BaseModel):
    tickets: List[Ticket]


class TicketUpdate(BaseModel):
    title: str
    description: str