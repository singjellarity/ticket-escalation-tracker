# Ticket Escalation Tracker

A Python-based ticket management and escalation tracking system built using SQLite. This project simulates a real-world customer support workflow, allowing users to create, manage, assign, and analyze support tickets through a command-line interface.

The application was designed to strengthen backend development, database management, SQL, and operational analytics skills while reflecting realistic customer support processes.

---

# Features

## Ticket Management
- Create support tickets
- View all tickets
- Update ticket statuses
- Delete tickets
- Assign tickets to agents

---

## Escalation System
- Automatically escalates high-priority tickets
- Tracks escalation status per ticket

---

# Database Integration
- SQLite database persistence
- SQL-based CRUD operations
- Relational table structure

---

# Analytics Dashboard
The project includes an analytics dashboard that displays:
- Total tickets
- Open tickets
- Escalated tickets
- Ticket status distribution
- Issue type analysis
- Agent workload analysis

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

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/singjellarity/ticket-escalation-tracker.git
```

---

## 2. Navigate to the Project Folder

```bash
cd ticket-escalation-tracker
```

---

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate
```

---

## 5. Install Required Packages

```bash
pip install matplotlib
```

---

# Running the Application

```bash
python main_sqlite_version.py
```

---

# Application Menu

```text
1. Create Ticket
2. View Tickets
3. Update Ticket Status
4. Delete Ticket
5. Assign Agent
6. Analytics Dashboard
7. Exit
```

---

# Example Analytics

The dashboard can visualize:
- Ticket status distribution
- Most common issue types
- Escalation trends
- Tickets per assigned agent

---

# Future Improvements

- FastAPI backend integration
- Web-based dashboard
- Authentication system
- PostgreSQL integration
- Search and filtering
- CSV export
- Docker support
- Cloud deployment

---

# Learning Outcomes

This project demonstrates:
- CRUD operations
- SQL integration with Python
- SQLite database management
- Data visualization
- Input validation
- Backend application logic
- Operational workflow modeling
- Git/GitHub version control

---

# Author

Mary Majella Imperial

GitHub:
https://github.com/singjellarity