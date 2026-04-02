from app.db.database import get_connection
from app.core.logger import logger

def get_all_tickets():
    conn = get_connection()

    cursor = conn.cursor()

    logger.info("Fetching tickets from DB")

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