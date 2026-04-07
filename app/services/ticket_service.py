"""
Ticket Service Layer.

Contains business logic for ticket operations.
Includes database connection and data transformations.
"""
from app.db.database import get_connection
from app.core.logger import logger
from fastapi import HTTPException

# Get tickets API
def get_all_tickets():
    conn = get_connection()

    cursor = conn.cursor()

    logger.info(
        "ticket.fetch",
        extra={
            "count": len(tickets)
        }
    )

    cursor.execute("SELECT id, title FROM tickets")
    rows = cursor.fetchall()

    tickets = []
    for row in rows:
        tickets.append({
            "id": row[0],
            "title": row[1]
        })

    logger.info(f"Fetched {len(tickets)} tickets")

    return {"tickets": tickets}

# Create tickets API
def create_ticket(title: str, description: str):
    conn = get_connection()
    cursor = conn.cursor()

    logger.info(
            "ticket.create",
            extra={
                "title": title
            }
    )

    cursor.execute(
        "INSERT INTO tickets (title, description, status) VALUES (?, ?, ?)",
        (title, description, "open")
    )

    conn.commit()

    logger.info("Ticket inserted successfully")

    return {"message": "Ticket created"}

# Update tickets
def update_ticket(ticket_id: int, title: str, description: str):
    conn = get_connection()
    cursor = conn.cursor()

    logger.info(
        "ticket.update",
        extra={
            "ticket_id": ticket_id
        }
    )

    cursor.execute(
        "UPDATE tickets SET title = ?, description = ? WHERE id = ?",
        (title, description, ticket_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        logger.warning(f"Ticket {ticket_id} not found")
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    logger.info(f"Ticket {ticket_id} updated successfully")

    return {"message": "Ticket updated"}

# Close Tickets
def close_ticket(ticket_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    logger.info(
        "ticket.close",
        extra={
            "ticket_id": ticket_id
        }
    )

    cursor.execute(
        "UPDATE tickets SET status = ? WHERE id = ?",
        ("closed", ticket_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        logger.warning(f"Ticket {ticket_id} not found")
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    logger.info(f"Ticket {ticket_id} closed successfully")

    return {"message": "Ticket closed"}