# Ticket Escalation Tracker

A Python and SQLite-based ticket management system designed to simulate real-world customer support workflows. The application allows users to create, manage, track, and analyze support tickets while maintaining activity logs and escalation tracking.

## Features

* Create, view, update, and delete tickets
* Assign tickets to agents
* Automatic escalation tracking for high-priority tickets
* Search tickets by customer, issue type, status, or assigned agent
* Ticket comments and activity logs
* Created and updated timestamps
* Analytics dashboard with visualizations

## Tech Stack

* Python
* SQLite
* SQL
* Matplotlib
* Git & GitHub

## Database Design

### Tickets

* Ticket information
* Status tracking
* Escalation flag
* Agent assignment
* Audit timestamps

### Ticket Comments

* Comment history
* Activity logs
* One-to-many relationship with tickets

## Installation

```bash
git clone https://github.com/singjellarity/ticket-escalation-tracker.git
cd ticket-escalation-tracker

python -m venv venv

# Windows
.\venv\Scripts\Activate

pip install matplotlib

python main_sqlite_version.py
```

## Key Concepts Demonstrated

* CRUD Operations
* SQLite Database Integration
* SQL Queries
* Search & Filtering
* Activity Logging
* One-to-Many Database Relationships
* Data Visualization
* Input Validation
* Git Version Control

## Future Improvements

* FastAPI REST API
* Streamlit Dashboard
* PostgreSQL Integration
* User Authentication
* Cloud Deployment

## Author

**Mary Majella Imperial**

GitHub: https://github.com/singjellarity

LinkedIn: https://www.linkedin.com/in/majellaimperial/
