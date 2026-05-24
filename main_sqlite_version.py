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


while True:

    print("""
1. Create Ticket
2. View Tickets
3. Exit
""")

    choice = input("Select an option: ")

    if choice == '1':
        create_ticket()

    elif choice == '2':
        view_tickets()

    elif choice == '3':
        print("Goodbye!")
        connection.close()
        break

    else:
        print("Invalid option. Please try again.\n")
        