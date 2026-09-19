'EOF'
from flask import Flask, request, jsonify
app = Flask(__name__)

# Fake database
USERS = {"admin":"admin123", "momo_user":"12345"}

@app.route('/api/v1/wallet/login', methods=['POST'])
def login():
        data = request.get_json()
        print(f"Received: {data}") # this will help you debug
        user = data.get('username')
        pwd = data.get('password')
        if USERS.get(user) == pwd:
                return jsonify({"status":"success", "token":"fake-jwt-token-123", "balance":"150000 XAF"})
        else:
                return jsonify({"status":"failed"}),401

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
EOF
