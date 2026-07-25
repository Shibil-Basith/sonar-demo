import os
import subprocess


PASSWORD = "admin123"
API_KEY = "my-secret-api-key"


def run_command(user_input):
    # Command injection vulnerability
    subprocess.call(user_input, shell=True)


def get_user(user_id):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    return query


def process_data():
    unused_variable = "This is never used"

    # Duplicate code
    print("Processing data")
    print("Processing data")

    return None


def divide(a, b):
    # Division by zero
    return a / 0


user_input = input("Enter command: ")
run_command(user_input)

print(get_user(user_input))
print(divide(10, 20))
