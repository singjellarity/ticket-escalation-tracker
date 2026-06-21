from database import cursor, connection
from datetime import datetime

# Add Comment Functionality
def add_comment():
    
    ticket_id = input("Enter Ticket ID: ")
    
    cursor.execute("""
    SELECT *
    FROM tickets
    WHERE id = ?
    """, (ticket_id,))
    
    ticket = cursor.fetchone()
    
    if not ticket:
        print("\nTicket not found.\n")
        return  
    
    comment = input("Enter your comment: ")
    
    if not comment.strip():
        print("\nComment cannot be empty.\n")
        return  
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
    INSERT INTO ticket_comments (
        ticket_id,
        comment,
        created_at
    )
    VALUES (?, ?, ?)
    """, (
        ticket_id,
        comment,
        current_time
    ))
    
    connection.commit()
    
    print("\nComment added successfully!\n")
    
# View Comments Functionality
def view_comments():
    
    ticket_id = input (
        "Enter ticket ID to view comments: "
    )
    cursor.execute("""
    SELECT *
    FROM ticket_comments
    WHERE ticket_id = ?
    """, (ticket_id,))
    
    comments = cursor.fetchall()
    
    if not comments:
        print("\nNo comments found for this ticket.\n")
        return

    print(f"\n--- Comments --- ")
    
    for comment in comments:
        print(f"[{comment[3]}] {comment[2]}")
        
# Log Activity Functionality
def log_activity(ticket_id, activity):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
    INSERT INTO ticket_comments (
        ticket_id,
        comment,
        created_at
    )
    VALUES (?, ?, ?)
    """, (
        ticket_id,
        activity,
        current_time
    ))
    connection.commit()