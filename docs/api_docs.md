# Transactions API Documentation

This API manages SMS transactions, allowing clients to **create, read, update, and delete transactions**. All endpoints require **Basic Authentication**.

**Authentication Credentials:**  
- Username: `admin`  
- Password: `password`  

All requests must include the header:  

Authorization: Basic <base64_encoded_username:password>


---

## 1. Get All Transactions

- **Endpoint & Method:**

GET /transactions


- **Request Example:**  
```http
GET /transactions
Headers:
Authorization: Basic YWRtaW46cGFzc3dvcmQ=

Response Example (200 OK):

[
  {
    "id": "tx001",
    "amount": 100.50,
    "sender_name": "Alice",
    "receiver_name": "Bob",
    "action": "send"
  },
  {
    "id": "tx002",
    "amount": 50.00,
    "sender_name": "Charlie",
    "receiver_name": "David",
    "action": "receive"
  }
]

Error Codes:
| Code | Description |
|------|-------------|
| 401 | Unauthorized (invalid or missing credentials) |

Error Codes:
| Code | Description |
|------|-------------|
| 401 | Unauthorized (invalid or missing credentials) |

Response Example (200 OK):

{
  "id": "tx001",
  "amount": 100.50,
  "sender_name": "Alice",
  "receiver_name": "Bob",
  "action": "send"
}

Error Codes:
| Code | Description |
|------|-------------|
| 401 | Unauthorized |
| 404 | Transaction not found |

Create a New Transaction

Endpoint & Method:

POST /transactions


Request Example:

POST /transactions
Headers:
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
Content-Type: application/json

{
  "id": "tx003",
  "amount": 75.25,
  "sender_name": "Eve",
  "receiver_name": "Frank",
  "action": "send"
}

Response Example (201 Created):

{
  "id": "tx003",
  "amount": 75.25,
  "sender_name": "Eve",
  "receiver_name": "Frank",
  "action": "send"
}


Error Codes:
| Code | Description |
|------|-------------|
| 400 | Empty body / Invalid JSON / Missing required fields / Transaction ID already exists |
| 401 | Unauthorized |

Update an Existing Transaction

Endpoint & Method:

PUT /transactions/{id}


Request Example:

PUT /transactions/tx003
Headers:
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
Content-Type: application/json

{
  "amount": 80.00,
  "receiver_name": "Grace"
}

Response Example (200 OK):

{
  "id": "tx003",
  "amount": 80.00,
  "sender_name": "Eve",
  "receiver_name": "Grace",
  "action": "send"
}

Error Codes:
| Code | Description |
|------|-------------|
| 400 | Empty body / Invalid JSON / No updatable fields provided |
| 401 | Unauthorized |
| 404 | Transaction not found |

Delete a Transaction

Endpoint & Method:

DELETE /transactions/{id}

Request Example:

DELETE /transactions/tx003
Headers:
Authorization: Basic YWRtaW46cGFzc3dvcmQ=

Response Example (200 OK):

{
  "message": "Transaction tx003 deleted"
}


Error Codes:
| Code | Description |
|------|-------------|
| 401 | Unauthorized |
| 404 | Transaction not found |
