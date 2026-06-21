from database import connection
from database import cursor

from ticket_service import (
    create_ticket,
    view_tickets,
    update_ticket_status,
    delete_ticket,
    assign_agent,
    search_tickets
)

from comments import (
    add_comment,
    view_comments
)

from analytics import analytics_dashboard

while True:

    print("""
1. Create Ticket
2. View Tickets
3. Update Ticket Status
4. Delete Ticket
5. Assign Agent
6. Analytics Dashboard
7. Search Tickets
8. Add comment
9. View comments
10. Exit
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
        add_comment()
        
    elif choice == '9':
        view_comments()
        
    elif choice == '10':
        print("Goodbye!")
        connection.close()
        break

    else:
        print("Invalid option. Please try again.\n")