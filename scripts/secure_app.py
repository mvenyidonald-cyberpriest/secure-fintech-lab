from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time

app = Flask(__name__)
# 1. Rate Limiting: 5 attempts per minute
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

USERS = {"admin":"complex_password_!@#2024"}

# 2. Implement Account Lockout logic + Logging
failed_attempts = {}

@app.route('/api/v1/wallet/login', methods=['POST'])
@limiter.limit("5 per minute")
def secure_login():
        data = request.get_json()
        ip = request.remote_addr

        # 3. INPUT VALIDATION
        if not data or len(data.get('password',''))<8:
                return jsonify({"error": "Invalid input"}), 400

        # Check if locked
        if failed_attempts.get(ip, 0)>=5:
                return jsonify({"error":"Account locked. Try after 15 mins"}), 429

        if USERS.get(data.get('username'))== data.get('password'):
                failed_attempts[ip]=0
                return jsonify({"status": "success", "message":"Use 2FA now"})
        else:
                failed_attempts[ip] = failed_attempts.get(ip, 0)+1
                # 4. Logging for SIEM
                print(f"[ALERT] Failed login for {data.get('username')} from {ip}")
                return jsonify({"status":"failed"}), 401


if __name__ == '__main__':
        app.run(port=8001)
