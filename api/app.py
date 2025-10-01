import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
from base64 import b64decode
import os

# Resolve path to data.json relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'dsa', 'data.json')

# Load the SMS transactions from JSON
with open(os.path.normpath(DATA_PATH), 'r', encoding='utf-8') as f:
    transactions = json.load(f)

# Basic authentication credentials
USERNAME = "admin"
PASSWORD = "password"

def check_auth(header):
    """Validate Basic Authentication header from client request"""
    if not header:
        return False
    try:
        auth_type, encoded = header.split()
        if auth_type != "Basic":
            return False
        decoded = b64decode(encoded).decode()
        user, pwd = decoded.split(":")
        return user == USERNAME and pwd == PASSWORD
    except:
        return False

def find_transaction(tx_id):
    """Search for a transaction by its ID in the transactions list"""
    for tx in transactions:
        if tx["id"] == tx_id:
            return tx
    return None

def save_transactions():
    """Write the updated transactions list back to data.json"""
    with open(os.path.normpath(DATA_PATH), 'w', encoding='utf-8') as f:
        json.dump(transactions, f, indent=2)

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code=200, content_type="application/json"):
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    # GET method
    def do_GET(self):
        """Handle GET requests: fetch all transactions or a specific one"""
        if not check_auth(self.headers.get('Authorization')):
            self._set_headers(401)
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return

        parsed_path = urllib.parse.urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")

        if parsed_path.path == "/transactions":
            self._set_headers()
            self.wfile.write(json.dumps(transactions).encode())
        elif len(path_parts) == 2 and path_parts[0] == "transactions":
            tx = find_transaction(path_parts[1])
            if tx:
                self._set_headers()
                self.wfile.write(json.dumps(tx).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    # POST method (add new transaction)
    def do_POST(self):
        """Handle POST requests: create a new transaction"""
        if not check_auth(self.headers.get('Authorization')):
            self._set_headers(401)
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return

        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path != "/transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())
            return

        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Empty body"}).encode())
            return

        body = self.rfile.read(content_length).decode('utf-8')
        try:
            data = json.loads(body)
        except Exception:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
            return

        # Ensure required fields
        required_fields = ["id", "amount", "sender_name", "receiver_name", "action"]
        if not all(f in data for f in required_fields):
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Missing required fields"}).encode())
            return

        # Check if ID already exists so as to Prevent duplicate IDs
        if find_transaction(data["id"]):
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Transaction with this ID already exists"}).encode())
            return

        transactions.append(data)
        save_transactions()
        self._set_headers(201)
        self.wfile.write(json.dumps(data).encode())

    # PUT method (update transaction)
    def do_PUT(self):
        """Handle PUT requests: update an existing transaction"""
        if not check_auth(self.headers.get('Authorization')):
            self._set_headers(401)
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return

        parsed_path = urllib.parse.urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")
        if len(path_parts) != 2 or path_parts[0] != "transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())
            return

        tx = find_transaction(path_parts[1])
        if not tx:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
            return

        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Empty body"}).encode())
            return

        body = self.rfile.read(content_length).decode('utf-8')
        try:
            data = json.loads(body)
        except Exception:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
            return

         # Only allow updating selected fields
        allowed_fields = ["amount", "sender_name", "receiver_name", "action"]
        updated = False
        for k, v in data.items():
            if k in allowed_fields:
                tx[k] = v
                updated = True

        if not updated:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "No updatable fields provided"}).encode())
            return

        save_transactions()
        self._set_headers(200)
        self.wfile.write(json.dumps(tx).encode())

    # DELETE method
    def do_DELETE(self):
        """Handle DELETE requests: remove a transaction by ID"""
        if not check_auth(self.headers.get('Authorization')):
            self._set_headers(401)
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return

        parsed_path = urllib.parse.urlparse(self.path)
        path_parts = parsed_path.path.strip("/").split("/")
        if len(path_parts) != 2 or path_parts[0] != "transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())
            return

        tx = find_transaction(path_parts[1])
        if not tx:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
            return

        transactions.remove(tx)
        save_transactions()
        self._set_headers(200)
        self.wfile.write(json.dumps({"message": f"Transaction {tx['id']} deleted"}).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    """Start the HTTP server on the given port"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

