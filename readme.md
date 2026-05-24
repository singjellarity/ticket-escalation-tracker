# Ticket Escalation Tracker

A Python-based ticket management system designed to simulate real-world customer support and escalation workflows. This project allows users to create, manage, update, assign, and analyze support tickets using a SQLite database backend.

The project was built to strengthen backend development, database management, and operational analytics skills while reflecting real customer support processes.

---

# Features

## Ticket Management
- Create support tickets
- View all tickets
- Update ticket status
- Delete tickets
- Assign tickets to agents

---

## Escalation Logic
- Automatically escalates high-priority tickets
- Tracks escalation status per ticket

---

## Database Integration
- SQLite database persistence
- Relational table structure
- CRUD operations using SQL queries

---

## Validation & Error Handling
- Ticket existence validation
- Status validation
- Delete confirmation prompts
- Graceful handling of invalid inputs

---

## Analytics Dashboard
- Total ticket count
- Open ticket count
- Escalated ticket count
- Ticket status distribution
- Ticket issue analysis
- Agent workload visualization

Charts are generated using Matplotlib.

---

# Technologies Used

- Python
- SQLite3
- SQL
- Matplotlib
- Git & GitHub
- VS Code

---


# Database Schema

## tickets table

| Column | Type |
|---|---|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| customer | TEXT |
| issue | TEXT |
| priority | TEXT |
| status | TEXT |
| escalated | BOOLEAN |
| assigned_agent | TEXT |

---

# Project Structure

```text
ticket-escalation-tracker/
│
├── venv/
├── main.py
├── main_sqlite_version.py
├── tickets.db
├── README.md
├── .gitignore
```
## File Explanation
- main_json_version.py is the original Python file used. Tickets created are stored in a JSON database
- main_sqlite_version.py is the updated Python file with all the improvements. Tickets created are stored in a database accessible using SQLite
- tickets.db is the database file accessible using SQLite
- tickets.json is the JSON file for the tickets created