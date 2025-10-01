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
```
Error Codes:

401: Unauthorized

# 2. Get Transaction by ID

Endpoint & Method:
GET /transactions/{id}

Request Example:

vbnet
GET /transactions/tx001
Headers:
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
Response Example (200 OK):

```json
{
  "id": "tx001",
  "amount": 100.50,
  "sender_name": "Alice",
  "receiver_name": "Bob",
  "action": "send"
}
```
Error Codes:

401: Unauthorized

404: Transaction not found

# 3. Create a New Transaction

Endpoint & Method:
POST /transactions

Request Example:

```json
{
  "id": "tx003",
  "amount": 75.25,
  "sender_name": "Eve",
  "receiver_name": "Frank",
  "action": "send"
}
```
Response Example (201 Created):

```json
{
  "id": "tx003",
  "amount": 75.25,
  "sender_name": "Eve",
  "receiver_name": "Frank",
  "action": "send"
}
```
Error Codes:

400: Empty body / Invalid JSON / Missing required fields / Transaction ID already exists

401: Unauthorized

# 4. Update an Existing Transaction

Endpoint & Method:
PUT /transactions/{id}

Request Example:

```json
{
  "amount": 80.00,
  "receiver_name": "Grace"
}
```
Response Example (200 OK):

```json
{
  "id": "tx003",
  "amount": 80.00,
  "sender_name": "Eve",
  "receiver_name": "Grace",
  "action": "send"
}
```
Error Codes:

400: Empty body / Invalid JSON / No updatable fields provided

401: Unauthorized

404: Transaction not found

# 5. Delete a Transaction

Endpoint & Method:
DELETE /transactions/{id}

Request Example:

makefile
DELETE /transactions/tx003
Headers:
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
Response Example (200 OK):

```json
{
  "message": "Transaction tx003 deleted"
}
```
Error Codes:

401: Unauthorized

404: Transaction not found

