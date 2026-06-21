from database import cursor, connection
from comments import log_activity
from datetime import datetime

def display_tickets(tickets):

    if not tickets:
        print("\nNo tickets found.\n")
        return

    for ticket in tickets:

        print(f"""
Ticket ID: {ticket[0]}
Customer: {ticket[1]}
Issue: {ticket[2]}
Priority: {ticket[3]}
Status: {ticket[4]}
Escalated: {"Yes" if ticket[5] else "No"}
Assigned Agent: {ticket[6] if ticket[6] else "Unassigned"}
Created At: {ticket[7] if len(ticket) > 7 and ticket[7] else "N/A"}
Updated At: {ticket[8] if len(ticket) > 8 and ticket[8] else "N/A"}
""")
        
# Ticket Creation Functionality 
def create_ticket():
    customer = input("Customer Name: ")
    issue = input("Issue Type: ")
    priority = input("Priority (Low/Medium/High): ")
    validate_priorities = ["Low", "Medium", "High"]
    
    if priority.title() not in validate_priorities:
        print("\nInvalid priority. Please enter Low, Medium, or High.\n")
        return

    escalated = priority.lower() == "high"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
    INSERT INTO tickets (
        customer,
        issue,
        priority,
        status,
        escalated,
        created_at,
        updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        customer,
        issue,
        priority,
        "Open",
        escalated,
        current_time,
        current_time
    ))

    connection.commit()
    ticket_id = cursor.lastrowid
    
    log_activity(
        ticket_id,
        f"Ticket created" 
    )

    print("\nTicket created successfully!\n")
    
# Ticket Viewing Functionality s
def view_tickets():

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    display_tickets(tickets)

# Update ticket status Functionality 
def update_ticket_status():
    
    ticket_id = input("Enter Ticket ID: ")

    cursor.execute("""
    SELECT * FROM tickets
    WHERE id = ?
    """, (ticket_id,))
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ticket = cursor.fetchone()

    if not ticket:
        print("\nTicket not found.\n")
        return

    old_status = ticket[4]

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

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    UPDATE tickets
    SET status = ?, updated_at = ?
    WHERE id = ?
    """, (
        new_status,
        current_time,
        ticket_id
    ))

    connection.commit()
    
    log_activity(
        ticket_id,
        f"Status changed from {old_status} to {new_status}"
    )

    print("\nTicket status updated successfully!\n")
    
# Delete Ticket Functionality
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
    
# Assign Agent Functionality 
def assign_agent():
    ticket_id = input("Enter Ticket ID: ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
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

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
    UPDATE tickets
    SET assigned_agent = ?, updated_at = ?
    WHERE id = ?
    """, (
        agent_name,
        current_time,
        ticket_id
    ))

    connection.commit()
    
    log_activity(
        ticket_id,
        f"Assigned to agent: {agent_name}"
    )

    print("\nAgent assigned successfully!\n")
     
# Search Tickets Functionality 
def search_tickets():

    print("""
Search By:
1. Customer Name
2. Issue Type
3. Status
4. Assigned Agent
""")

    choice = input("Select search option: ")

    if choice == "1":
        customer = input("Enter customer name: ")

        cursor.execute("""
        SELECT *
        FROM tickets
        WHERE customer LIKE ?
        """, (f"%{customer}%",))

    elif choice == "2":
        issue = input("Enter issue type: ")

        cursor.execute("""
        SELECT *
        FROM tickets
        WHERE issue LIKE ?
        """, (f"%{issue}%",))

    elif choice == "3":
        status = input(
            "Enter status (Open/In Progress/Closed): "
        ).title()

        cursor.execute("""
        SELECT *
        FROM tickets
        WHERE status = ?
        """, (status,))

    elif choice == "4":
        agent = input("Enter assigned agent name: ")

        cursor.execute("""
        SELECT *
        FROM tickets
        WHERE assigned_agent LIKE ?
        """, (f"%{agent}%",))

    else:
        print("\nInvalid option.\n")
        return

    results = cursor.fetchall()

    display_tickets(results)