import sqlite3
from datetime import datetime

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    issue TEXT,
    priority TEXT,
    status TEXT,
    escalated BOOLEAN,
    assigned_agent TEXT,
    created_at TEXT,
    updated_at TEXT
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

import matplotlib.pyplot as plt

import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime



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

    print("\nTicket created successfully!\n")

def display_tickets(tickets):
    if not tickets:
        prrint("\nNo tickets found.\n")
        returrn
        
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
        
def view_tickets():

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    if not tickets:
        print("\nNo tickets found.\n")
        return

    print("\n--- Ticket List ---")

    for ticket in tickets:
        display_tickets([ticket])

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
    SET status = ?, updated_at = ?
    WHERE id = ?
    """, (
        new_status,
        current_time,
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

    print("\nAgent assigned successfully!\n")
   
def analytics_dashboard():
    
    print("\n--- Ticket Analytics Dashboard ---\n")
    
    ##Total Tickets KPI
    cursor.execute("""
    SELECT COUNT(*) FROM tickets
    """)

    total_tickets = cursor.fetchone()[0]

    print(f"Total Tickets: {total_tickets}")
    
    ##Open Tickets KPI
    cursor.execute("""
    SELECT COUNT(*) FROM tickets
    WHERE status = 'Open'
    """)

    open_tickets = cursor.fetchone()[0]

    print(f"Open Tickets: {open_tickets}")
    
    ##Escalated Tickets KPI
    cursor.execute("""
    SELECT COUNT(*) FROM tickets
    WHERE escalated = 1
    """)

    escalated_tickets = cursor.fetchone()[0]

    print(f"Escalated Tickets: {escalated_tickets}")
    
    ##Status Distribution Query
    cursor.execute("""
    SELECT status, COUNT(*)
    FROM tickets
    GROUP BY status
    """)

    status_data = cursor.fetchall()
    
    ##Prepare Data for Visualization
    
    statuses = [row[0] for row in status_data]
    counts = [row[1] for row in status_data]
    

    
    plt.figure(figsize=(6,6))

    plt.pie(
        counts,
        labels=statuses,
        autopct='%1.1f%%'
    )

    plt.title("Ticket Status Distribution")

    plt.show()
    
    ##Issue Type Analysis
    cursor.execute("""
    SELECT issue, COUNT(*)
    FROM tickets
    GROUP BY issue
    """)

    issue_data = cursor.fetchall()

    issues = [row[0] for row in issue_data]
    issue_counts = [row[1] for row in issue_data]
    
    ##Create Bar Chart
    plt.figure(figsize=(8,5))

    plt.bar(issues, issue_counts)

    plt.title("Tickets by Issue Type")

    plt.xlabel("Issue Type")

    plt.ylabel("Number of Tickets")

    plt.show()
    
    ## Agent Workload Analysis
    cursor.execute("""
    SELECT assigned_agent, COUNT(*)
    FROM tickets
    WHERE assigned_agent IS NOT NULL
    GROUP BY assigned_agent
    """)

    agent_data = cursor.fetchall()

    if agent_data:

        agents = [row[0] for row in agent_data]
        ticket_counts = [row[1] for row in agent_data]

        plt.figure(figsize=(8,5))

        plt.bar(agents, ticket_counts)

        plt.title("Tickets per Agent")

        plt.xlabel("Agent")

        plt.ylabel("Assigned Tickets")

        plt.show() 
        
        try:
            cursor.execute("""
            ALTER TABLE tickets
            ADD COLUMN created_at TEXT
            """)
            
            connection.commit()
            
        except sqlite3.OperationalError:
            pass
        
        try:
            cursor.execute("""
            ALTER TABLE tickets
            ADD COLUMN updated_at TEXT
            """)
            
            connection.commit()
        except sqlite3.OperationalError:
            pass
        
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
        status = input("Enter status: ").title()
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

    if not results:
        print("\nNo tickets found.\n")
        return

    for ticket in results:
        display_tickets([ticket])
   
        
while True:

    print("""
1. Create Ticket
2. View Tickets
3. Update Ticket Status
4. Delete Ticket
5. Assign Agent
6. Analytics Dashboard
7. Search Tickets
8. Exit
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
        analytics_dashboard()  
             

    elif choice == '7':
        search_tickets()

    elif choice == '8':
        print("Goodbye!")
        connection.close()
        break

    else:
        print("Invalid option. Please try again.\n")
        
        
