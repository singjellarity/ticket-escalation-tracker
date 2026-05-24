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

try:
    cursor.execute("""
    ALTER TABLE tickets
    ADD COLUMN assigned_agent TEXT
    """)

    connection.commit()

except sqlite3.OperationalError:
    pass



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
Assigned Agent: {ticket[6] if ticket[6] else "Unassigned"}
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
    
def delete_ticket():

    ticket_id = input("Enter Ticket ID to delete: ")

    cursor.execute("""
    SELECT * FROM tickets
    WHERE id = ?
    """, (ticket_id,))

    ticket = cursor.fetchone()

    if not ticket:
        print("\nTicket not found.\n")
        return
    
    while True:

        confirmation = input(
            "Are you sure you want to delete this ticket? (yes/no): "
        ).strip().lower()

        if confirmation in ["yes", "y"]:
            break

        elif confirmation in ["no", "n"]:
            print("\nDeletion cancelled.\n")
            return

        else:
            print("\nPlease enter yes or no.\n")


    cursor.execute("""
    DELETE FROM tickets
    WHERE id = ?
    """, (ticket_id,))

    connection.commit()

    print("\nTicket deleted successfully!\n")

def assign_agent():

    ticket_id = input("Enter Ticket ID: ")

    cursor.execute("""
    SELECT * FROM tickets
    WHERE id = ?
    """, (ticket_id,))

    ticket = cursor.fetchone()

    if not ticket:
        print("\nTicket not found.\n")
        return

    agent_name = input("Enter agent name: ").strip()

    if not agent_name:
        print("\nAgent name cannot be empty.\n")
        return

    cursor.execute("""
    UPDATE tickets
    SET assigned_agent = ?
    WHERE id = ?
    """, (
        agent_name,
        ticket_id
    ))

    connection.commit()

    print("\nAgent assigned successfully!\n")
    
    
while True:

    print("""
1. Create Ticket
2. View Tickets
3. Update Ticket Status
4. Delete Ticket
5. Assign Agent
6. Exit
""")

    choice = input("Select an option: ")

    if choice == '1':
        create_ticket()

    elif choice == '2':
        view_tickets()

    elif choice == '3':
        update_ticket_status()

    elif choice == '4':
        delete_ticket()

    elif choice == '5':
        assign_agent()

    elif choice == '6':
        print("Goodbye!")
        connection.close()
        break

    else:
        print("Invalid option. Please try again.\n")
        