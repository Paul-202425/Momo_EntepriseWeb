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







# ALU MoMo REST API (Plain Python `http.server`)

A minimal REST API built **without frameworks** using Python's standard library to expose Mobile Money (MoMo) SMS transaction data. Includes:

- XML → JSON parser
- CRUD endpoints
- Basic Authentication
- Data structure & algorithm (DSA) comparison: linear search vs dictionary lookup
- Docs, sample cURL tests, and a report template

---

## Project Structure

```
Momo_EntepriseWeb/
├─ api/
│   └─ app.py                     # REST API server with CRUD + Basic Auth
│
├─ database/
│   ├─ database_setup.sql         # SQL schema (Users, Transactions, Categories, etc.)
│   └─ ERD Image.pdf              # Entity-Relationship Diagram (ERD)
│
├─ docs/
│   └─ api_docs.md                # API endpoint documentation
│
├─ dsa/
│   ├─ parse_xml.py               # Parses modified_sms_v2.xml → JSON
│   └─ search_bench.py            # Benchmarks linear vs dict lookup
│
├─ examples/
│   └─ (sample/test files if any) # For trials, practice, or sample snippets
│
├─ projectdocs/
│   ├─ Grp2 Database Design Document.pdf   # Detailed ERD design explanation
│   ├─ AI Usage Log.md                     # Log of AI assistance
│   └─ json_schemas.json                   # JSON schema mapping for DB tables
│
├─ report/
│   └─ report.md                 # Report draft (to be exported as PDF for submission)
│
├─ screenshots/
│   └─ images    # Postman/cURL screenshots: GET, POST, PUT, DELETE
│
├─ data.json                     # Parsed transaction data from XML
├─ modified_sms_v2.xml           # Original SMS dataset (input file)
└─ README.md                     # Project overview, objectives, setup instructions


## 1) Setup

**Requirements**: Python 3.10+ (standard library only)

```bash
cd ALU_MoMo_API
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install --upgrade pip
```

Optional: Place your dataset at `./modified_sms_v2.xml` or anywhere else and pass its path to the parser.

---

## 2) Parse XML → JSON

```bash
# From project root:
python dsa/parse_xml.py --xml ./modified_sms_v2.xml --out ./data/transactions.json
```

- If `--xml` is omitted or file not found, the parser will **generate 25 synthetic records** (good enough for DSA tests) and save to `data/transactions.json`.

---

## 3) Run the API

```bash
# From project root:
python api/server.py
```

**Defaults**:
- Host: `127.0.0.1`
- Port: `8080`
- Credentials: `admin : secret` (override with env vars `API_USER` and `API_PASS`)
- Data file: `./data/transactions.json` (auto-created if missing)

Environment overrides:
```bash
# Example
set API_USER=paul      # Windows (PowerShell: $env:API_USER="paul")
set API_PASS=strongpw
set API_HOST=0.0.0.0
set API_PORT=9090
set API_DATA=./data/transactions.json
```

---

## 4) cURL Tests (Screenshots required)

**Base64 helper**: `echo -n "admin:secret" | base64` → `YWRtaW46c2VjcmV0`
> Or just use `-u admin:secret` with curl.

### 4.1 Unauthorized example (401)
```bash
curl -i http://127.0.0.1:8080/transactions
```

### 4.2 Authorized GET all
```bash
curl -i -u admin:secret http://127.0.0.1:8080/transactions
```

### 4.3 Authorized GET one
```bash
curl -i -u admin:secret http://127.0.0.1:8080/transactions/3
```

### 4.4 POST (create)
```bash
curl -i -u admin:secret -H "Content-Type: application/json" -d "{
  \"type\": \"CASHIN\", \"amount\": 1200, \"sender\": \"0788000000\", \"receiver\": \"MERCHANT123\", \"timestamp\": \"2025-10-02T18:00:00\"
}" http://127.0.0.1:8080/transactions
```

### 4.5 PUT (update)
```bash
curl -i -u admin:secret -X PUT -H "Content-Type: application/json" -d "{
  \"amount\": 2000
}" http://127.0.0.1:8080/transactions/3
```

### 4.6 DELETE
```bash
curl -i -u admin:secret -X DELETE http://127.0.0.1:8080/transactions/3
```

> 📸 Add screenshots of: 1) successful GET with auth, 2) unauthorized GET, 3) successful POST, PUT, DELETE to `/screenshots/`.

---

## 5) Run DSA Benchmark

```bash
python dsa/search_bench.py --data ./data/transactions.json --trials 10000
```

This prints timings for:
- Linear search over a list
- O(1)-average dictionary lookup (`id → transaction`)

---

## 6) Documentation & Report

- Edit `docs/api_docs.md` with your examples/results.
- Fill `report/report.md`, then export as PDF for submission.

---

## 7) GitHub Upload

Initialize the repo and push:
```bash
git init
git add .
git commit -m "MoMo REST API: CRUD + Basic Auth + DSA benchmark"
git branch -M main
git remote add origin <https://github.com/Paul-202425/Momo_EntepriseWeb>
git push -u origin main
```

---

## Notes for Markers

- Built with only Python stdlib.
- Clean separation of concerns: parsing, API, DSA.
- Comprehensive documentation & screenshots.
