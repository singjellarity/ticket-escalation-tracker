import sqlite3

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    issue TEXT,
    priority TEXT,
    status TEXT,
    escalated BOOLEAN
)
""")

connection.commit()


def create_ticket():
    customer = input("Customer Name: ")
    issue = input("Issue Type: ")
    priority = input("Priority (Low/Medium/High): ")

    escalated = priority.lower() == "high"

    cursor.execute("""
    INSERT INTO tickets (
        customer,
        issue,
        priority,
        status,
        escalated
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        customer,
        issue,
        priority,
        "Open",
        escalated
    ))

    connection.commit()

    print("\nTicket created successfully!\n")


def view_tickets():

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    if not tickets:
        print("\nNo tickets found.\n")
        return

    print("\n--- Ticket List ---")

    for ticket in tickets:
        print(f"""
Ticket ID: {ticket[0]}
Customer: {ticket[1]}
Issue: {ticket[2]}
Priority: {ticket[3]}
Status: {ticket[4]}
Escalated: {"Yes" if ticket[5] else "No"}
""")

def update_ticket_status():

    ticket_id = input("Enter Ticket ID: ")

    cursor.execute("""
    SELECT * FROM tickets
    WHERE id = ?
    """, (ticket_id,))

    ticket = cursor.fetchone()

    if not ticket:
        print("\nTicket not found.\n")
        return

    new_status = input(
        "Enter new status (Open/In Progress/Closed): "
    ).title()

    valid_statuses = [
        "Open",
        "In Progress",
        "Closed"
    ]

    if new_status not in valid_statuses:
        print("\nInvalid status.\n")
        return

    cursor.execute("""
    UPDATE tickets
    SET status = ?
    WHERE id = ?
    """, (
        new_status,
        ticket_id
    ))

    connection.commit()

    print("\nTicket status updated successfully!\n")
    
    


while True:

    print("""
1. Create Ticket
2. View Tickets
3. Update Ticket Status
4. Exit
""")

    choice = input("Select an option: ")

    if choice == '1':
        create_ticket()

    elif choice == '2':
        view_tickets()

    elif choice == '3':
        update_ticket_status()

    elif choice == '4':
        print("Goodbye!")
        connection.close()
        break

    else:
        print("Invalid option. Please try again.\n")
        