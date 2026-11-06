import time
from company.branches import EMPLOYEES

MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 5

def check_credentials(username, password):
    """Check if the provided username and password are valid."""
    username.lower()
    employee = EMPLOYEES.get(username)

    if employee is None:
        return False

    return employee["password"] == password

def login():
    """Prompt the user for username and password, and return the username if valid."""
    attempts = 0

    while attempts != MAX_ATTEMPTS:
        username = input("Username: ").lower()
        password = input("Password: ")
        credentials = check_credentials(username, password)
        
        if credentials == False:
            attempts += 1
            print(f"Invalid username or password. Attempts left: {MAX_ATTEMPTS - attempts}")

        if credentials == True:
            return username

    print("Max attempts reached, lockout")
    time.sleep(LOCKOUT_SECONDS)
    return None