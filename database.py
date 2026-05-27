import sqlite3


def connect_db():

    conn = sqlite3.connect("tickets.db")

    return conn

def create_table():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            issue TEXT,
            severity TEXT,
            summary TEXT
        )
        """
    )

    conn.commit()

    conn.close()
create_table()

def save_ticket(issue, severity, summary):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets (issue, severity, summary)
        VALUES (?, ?, ?)
        """,
        (issue, severity, summary)
    )

    conn.commit()

    conn.close()

def get_all_tickets():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, issue, severity, summary
        FROM tickets
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def delete_ticket(ticket_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM tickets
        WHERE id = ?
        """,
        (ticket_id,)
    )

    conn.commit()

    conn.close()