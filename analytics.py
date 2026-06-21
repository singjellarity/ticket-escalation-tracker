from database import cursor
import matplotlib.pyplot as plt


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
        
        