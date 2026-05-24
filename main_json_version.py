import json
def save_tickets():
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)
        
def load_tickets():
    global tickets

    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        tickets = []


tickets = []

def create_ticket():
    customer = input("Customer Name: ")
    issue = input("Issue Type: ")
    priority = input("Priority (Low/Medium/High): ")
                     
    ticket = {
        "customer": customer,
        "issue": issue,
        "priority": priority,
        "status": "Open",
        "escalated": priority.lower() == "high"
    }
    tickets.append(ticket)
    save_tickets()    
    print("\nTicket created successfully!\n")
    
def view_tickets():
    if not tickets:
        print("\nNo tickets found.\n")
        return
    
    print("\n--- Ticket List ---")
    
    for index, ticket in enumerate(tickets, start=1):
        print (f"""
               
Ticket #{index}
Customer: {ticket['customer']}
Issue: {ticket['issue']}
Priority: {ticket['priority']}
Status: {ticket['status']}
Escalated: {"Yes" if ticket['escalated'] else "No"}

""")
        

load_tickets()


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
        break
    else:
        print("Invalid option. Please try again.\n")