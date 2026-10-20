import os
import requests
from flask import Flask, jsonify
app = Flask(__name__)
BASE_SHIFT = int(os.environ.get('SYSTEM_SHIFT', 2))
ADMIN_IP_CIPHERED = os.environ.get('ADMIN_IP_CIPHERED', '349.78.472.38') 
def dynamic_caesar_cipher(text, start_s):
    result = ""
    current_shift = start_s
    for char in text:
        if char.isdigit():
            result += str((int(char) + current_shift) % 10)
            current_shift += 2
        else:
            result += char
    return result
def get_current_ip():
    try:
        response = requests.get('https://ipify.org', timeout=5)
        return response.text.strip()
    except requests.RequestException:
        return None

@app.route('/check-admin')
def monitor_ip():
    current_ip = get_current_ip()
    if not current_ip:
        return jsonify({"error": "IP not found"}), 500
    
    ciphered_input = dynamic_caesar_cipher(current_ip, BASE_SHIFT)
    
    if ciphered_input == ADMIN_IP_CIPHERED:
        return jsonify({"status": "Access granted", "IP": current_ip}), 200
    else:
        return jsonify({"status": "Access denied", "IP": current_ip}), 403

if __name__ == '__main__':
    app.run(host='192.168.1.1', port=443)