"""
Ticket Service Layer.

Contains business logic for ticket operations.
Includes database connection and data transformations.
"""
from app.db.database import get_connection
from app.core.logger import logger


# Get tickets API
def get_all_tickets():
    conn = get_connection()

    cursor = conn.cursor()

    logger.info("ticket.fetch")

    cursor.execute("SELECT id, title FROM tickets")
    rows = cursor.fetchall()

    tickets = []

    for row in rows:
        tickets.append({
            "id": row[0],
            "title": row[1]
        })

    logger.info(
        "ticket.fetched",
        extra={
            "count": len(tickets)
        }
    )

    return {"tickets": tickets}

# Create tickets API
def create_ticket(title: str, description: str):
    conn = get_connection()
    cursor = conn.cursor()

    logger.info(f"Inserting ticket into DB | title={title}")

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

    logger.info("Updating ticket {ticket_id}")

    cursor.execute(
        "UPDATE tickets SET title = ?, description = ? WHERE id = ?",
        (title, description, ticket_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        logger.warning(f"Ticket {ticket_id} not found")
        return {"error": "Ticket not found"}
    
    logger.info(f"Ticket {ticket_id} updated successfully")

    return {"message": "Ticket updated"}

# Close Tickets
def close_ticket(ticket_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    logger.info(f"Closing ticket {ticket_id}")

    cursor.execute(
        "UPDATE tickets SET status = ? WHERE id = ?",
        ("closed", ticket_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        logger.warning(f"Ticket {ticket_id} not found")
        return {"error": "Ticket not found"}
    
    logger.info(f"Ticket {ticket_id} closed succeessfully")

    return {"message": "Ticket closed"}