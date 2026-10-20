from argon2 import PasswordHasher
import time
import sys
import getpass
granted = 0
attempts = 0
def save_data(list_of_data):
    with open("data.txt", "w") as file:
        file.write("|".join(list_of_data))

def retrieve_data():
    try: 
        with open("data.txt", "r") as file:
            return file.read().split("|")
    except:
        with open("data.txt", "w") as _:
            return []

def update_logs(username):
    current_file = retrieve_data()
    new_logs = current_file + [username]
    save_data(new_logs)
    return new_logs

def password_check():
    ph = PasswordHasher()
    attempts_max = 5
    password = "$argon2id$v=19$m=65536,t=3,p=4$28L5myQ85xW9PCkrXg5r0g$vbypO7q6qvMmDb82SCCgrNQZJwOKwVy3dIYQvsZtK5o"
    username = "admin"
    password_detection = getpass.getpass("Password: ")
    username_detection = input("Username: ")
    time.sleep(0.1)
    try:
        if ph.verify(password, password_detection) and username_detection == username:
            granted = True
            print(" ".join(update_logs(username_detection)))
            print("[ACCES GRANTED]: ")    
        else:
            raise ValueError("[ACCESS DENIED]")
    except Exception:
        granted = False
        print(" ".join(update_logs(username_detection)))
        print("[ACCESS DENIED]")
        attempts += 1
        if attempts >= attempts_max:
            time.sleep(60)
            attempts = 0
while True:
    Continue = input("[0 TO EXIT 1 TO CONTINUE OPERATIONS]: ")
    if Continue == "1":  
        password_check()
    elif Continue == "0":
        print("[SHUTTING DOWN SYSTEM]")
        break