# Transactions API Documentation

This file documents the endpoints of the Transactions API. The API manages SMS transactions and supports **creating, reading, updating, and deleting transactions**.  

All endpoints require **Basic Authentication**.

**Authentication Credentials:**  
- Username: `admin`  
- Password: `password`  

All requests must include the header:  

Authorization: Basic <base64_encoded_username:password>


---

## 1. Get All Transactions

**Endpoint & Method:**  
`GET /transactions`

**Request Example:**  

GET /transactions
Headers:
Authorization: Basic YWRtaW46cGFzc3dvcmQ=


**Response Example (200 OK):**  
```json
[
  {
    "id": "tx001",
    "amount": 100.50,
    "sender_name": "Alice",
    "receiver_name": "Bob",
    "action": "send"
  }
]

---
##Error Codes:##

401: Unauthorized

2. Get Transaction by ID

Endpoint & Method:
GET /transactions/{id}

Request Example:
