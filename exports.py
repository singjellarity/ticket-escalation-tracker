import csv
from database import cursor

def export_tickets_to_csv():
    """Export tickets from the database to a CSV file.

    Inputs: None.
    Outputs: Creates 'tickets_export.csv' in the current working directory (UTF-8 encoded).
    Side effects: Writes the file and prints status messages.
    """
    cursor.execute("""
    SELECT * 
    FROM tickets
    """)
    
    tickets = cursor.fetchall()
    
    if not tickets:
        print("\nNo tickets to export.\n")
        return
    

    with open('tickets_export.csv', 
              'w', 
              newline='',
              encoding='utf-8'
              ) as f:        
        writer = csv.writer(f)
        writer.writerow([
            "Ticket ID",
            "Customer",
            "Issue",
            "Priority",
            "Escalated",
            "Status",
            "Assigned Agent",
            "Created At",
            "Updated At"
        ])
        for ticket in tickets:
            writer.writerow([
                ticket[0], #ID
                ticket[1], #Customer
                ticket[2], #Issue
                ticket[3], #Priority
                "Yes" if ticket[5] else "No",
                ticket[4], #Status
                ticket[6], #Assigned Agent
                ticket[7], #Created At
                ticket[8] #Updated Ats
            ])
    print("\nTickets exported successfully to tickets_export.csv\n")