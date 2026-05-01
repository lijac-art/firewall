import os
import requests
BASE_SHIFT = int(os.environ.get('SYSTEM_SHIFT', 2))
ADMIN_IP_CIPHERED = "349.78.472.38"
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
        response = requests.get('http://checkip.amazonaws.com')
        return response.text.strip()
    except requests.RequestException:
        return None
def monitor_ip():
    current_ip = get_current_ip()
    if not current_ip:
        print("Error: IP not found.")
        return False
    ciphered_input = dynamic_caesar_cipher(current_ip, BASE_SHIFT)
    if ciphered_input == ADMIN_IP_CIPHERED:
        print("Access granted: Welcome, admin!")
        return True
    else:
        print("Access denied.")
        return False
if __name__ == "__main__":
    monitor_ip()
