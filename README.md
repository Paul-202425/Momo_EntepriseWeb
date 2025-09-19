# Momo_EntepriseWeb

## 📌 Project Description
This project is part of a continuous formative assessment where we design and develop an enterprise-level full-stack application. The goal is to **process, clean, and analyze MoMo (Mobile Money) SMS transaction data** in XML format, store it in a relational database, and build a frontend interface for visualization and insights.

---

## 🌍 Project Overview
The system will:
- Ingest & parse MoMo SMS data in XML format.  
- Clean & categorize the data into meaningful transaction types (deposits, withdrawals, payments, transfers).  
- Store & manage the processed data in a relational database for efficient querying.  
- Visualize & analyze transactions through an intuitive frontend dashboard.  

---

## 🎯 Objectives
- Practice collaborative development workflows in a team setting.  
- Define and document the system architecture (backend, database, frontend).  
- Apply Agile practices to organize tasks and iterations.  
- Gain hands-on experience in backend processing, database management, and frontend development.  

---

## 📅 Week 1 Focus
- Set up the team’s shared workspace (repository, collaboration tools, workflows).  
- Defined the system architecture and selected the tech stack.  
- Created an Agile board (sprints, epics, tasks).  

---

## 🛠️ Tech Stack
- **Backend:** Node.js / Python (for XML parsing & processing)  
- **Database:** MySQL 8.x (primary) / PostgreSQL (alternative)  
- **Frontend:** React.js (with chart libraries for visualization)  
- **Collaboration:** GitHub Projects / Trello / Jira  

---

## 👥 Team – EWD Group 2
1. Gabriella Ange Ahirwe  
2. Kudakwashe Norman Chikovo  
3. Oriane Uwineza  
4. Paul Masamvu  
5. Samuel Chima Nkpado  

🔗 **Trello Board:** [Enterprise Web Development Board](https://trello.com/invite/b/68bde71e2a7c3f2073109e49/ATTIb12ed74dfb3852d1ce5ad01f5ce2f422419F377B/enterprise-web-development-g2)  

📐 **System Architecture:**  
![Group2 Diagram](https://github.com/user-attachments/assets/b4469cf7-86fc-41ea-afc4-4d989a8462e8)

---

# 📊 Database Design (Week 2 Focus)

## Overview
In Sprint 2, our focus shifted to designing and implementing the **database foundation** of the MoMo SMS data processing system. We created an **Entity Relationship Diagram (ERD)** to capture the key entities — *Users, Transactions, Transaction Categories, System Logs* — and introduced a junction table (*Transaction_Participants*) to resolve the many-to-many relationship between users and transactions.  

📁 The ERD is located here:  
`/docs/erd_diagram.png`  

---

## Schema Summary
- **Users** → stores customer details (`user_id, msisdn, full_name`).  
- **Transactions** → records core financial events (`tx_id, amount, datetime, category_id`).  
- **Transaction_Categories** → lookup table for transaction types (`category_id, code, name`).  
- **Transaction_Participants** → junction table linking users to transactions with roles (sender, receiver, merchant).  
- **System_Logs** → audit trail of processing events (`log_id, event_type, message, tx_id`).  

A detailed **Data Dictionary** with attributes, data types, PK/FK constraints, and comments is provided in:  
`/docs/Database_Design_Document.pdf`  

---

## 🔑 Design Rationale (200–300 words)
Our design follows a normalized relational structure to ensure data integrity and scalability. The **Users** table uniquely identifies customers using `user_id` and mobile numbers (`msisdn`), preventing duplication. The **Transactions** table acts as the core fact entity, recording each financial event with attributes such as `amount`, `datetime`, and links to transaction categories.  

To avoid redundancy, transaction types are abstracted into a **Transaction_Categories** lookup table, which ensures consistency in categorization (e.g., "deposit", "payment"). Since a transaction can involve multiple users (e.g., sender and receiver), we introduced the **Transaction_Participants** junction table. This resolves the many-to-many relationship by mapping each user’s role in a transaction, thereby improving flexibility and supporting scenarios like merchant transactions.  

Finally, the **System_Logs** table provides traceability of system operations, essential for auditing, debugging, and accountability. This enhances data governance and supports compliance.  

The model applies **referential integrity** using foreign keys to ensure that transactions cannot exist without valid users or categories. Indexes on frequently queried fields (e.g., `msisdn`, `datetime`) improve performance. By combining strong normalization with selective indexing, our schema balances data accuracy, query efficiency, and future extensibility — making it suitable for enterprise-level mobile money processing.  

---

## ⚙️ Setup Instructions
1. **Environment:** MySQL 8.x recommended.  
2. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/Momo_EntepriseWeb.git
   cd Momo_EntepriseWeb
