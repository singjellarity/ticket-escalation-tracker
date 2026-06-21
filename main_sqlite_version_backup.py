import sqlite3
from datetime import datetime

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()




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
Created At: {ticket[7]}
Updated At: {ticket[8]}
""")
        



    



   

        

   

    





        
        
