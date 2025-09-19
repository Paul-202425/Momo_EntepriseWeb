# Momo_EntepriseWeb

# Project_description
This project is part of a continuous formative assessment where we design and develop an enterprise-level fullstack application. The goal is to process, clean, and analyze MoMo (Mobile Money) SMS transaction data in XML format, store it in a relational database, and build a frontend interface for visualization and insights.

## PROJECT OVERVIEW
The system will:
- Ingest & Parse MoMo SMS data in XML format.
- Clean & Categorize the data into meaningful transaction types (e.g., deposits, withdrawals, payments, transfers).
- Store & Manage the processed data in a relational database for efficient querying.
- Visualize & Analyze transactions through an intuitive frontend dashboard.

## OBJECTIVES
- Practice collaborative development workflows in a team setting.
- Define and document the system architecture (backend, database, and frontend layers).
- Apply Agile practices to organize tasks and iterations.
- Gain hands-on experience in backend processing, database management, and frontend development.

## WEEK 1 FOCUS
For this first sprint, the primary goals were:
- Setting up the team’s shared workspace (repository, collaboration tools, and workflows).
- Defining the system architecture and tech stack.
- Creating an Agile board (sprints, epics, and tasks).

## TECH STACK (Proposed)
- **Backend:** Node.js / Python (for XML parsing & data processing)  
- **Database:** PostgreSQL / MySQL  
- **Frontend:** React.js (with chart libraries for visualization)  
- **Collaboration:** GitHub Projects / Jira (Agile task tracking)

---

# EWD_Group_2
### Team Members List
1. Gabriella Ange Ahirwe  
2. Kudakwashe Norman Chikovo  
3. Oriane Uwineza  
4. Paul Masamvu  
5. Samuel Chima Nkpado  

This is our **Trello link**:  
[Enterprise Web Development Board](https://trello.com/invite/b/68bde71e2a7c3f2073109e49/ATTIb12ed74dfb3852d1ce5ad01f5ce2f422419F377B/enterprise-web-development-g2)

This is our **System Architecture**:  
![Group2 Diagram](https://github.com/user-attachments/assets/b4469cf7-86fc-41ea-afc4-4d989a8462e8)

---

# 📊 Database Design (Week 2 Focus)

## Overview
In Sprint 2, our focus shifted to designing and implementing the **database foundation** of the MoMo SMS data processing system.  
We built an Entity Relationship Diagram (ERD) to capture key entities (Users, Transactions, Transaction Categories, System Logs) and resolved many-to-many relationships through a junction table for transaction participants.  
The ERD file can be found in:  
`/docs/erd_diagram.png`

---

## Schema Summary
- **Users** → stores customer details (user_id, msisdn, full_name).  
- **Transactions** → core financial events (tx_id, amount, datetime, category_id).  
- **Transaction_Categories** → lookup table for transaction types (category_id, code, name).  
- **Transaction_Participants** → junction table linking users to transactions with their role (sender, receiver, merchant).  
- **System_Logs** → audit trail of processing events (log_id, event_type, message, tx_id).  

A complete Data Dictionary with attributes, keys, and constraints is provided in `/docs/Database_Design_Document.pdf`.

---

## Setup Instructions
1. **Environment:** MySQL 8.x recommended.  
2. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/momo-sms-db.git
   cd momo-sms-db
