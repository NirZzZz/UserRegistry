import requests
from names_generator import generate_name
from db_connector import get_all_users, delete_user

# Test for posting new user to users database
name = generate_name()
URL = "http://127.0.0.1:5000/users"
payload = {"user_name": f"{name}"}
headers = {'Content-Type': 'application/json'}
r = requests.post(URL, json=payload, headers=headers)

# Check posted data was stored inside DB
all_users = get_all_users()
user_id = None
for user in all_users:
    if user['user_name'] == name:
        print(f"{name} found, test finish successfully")
        user_id = user['user_id']
        break

# If user is found, delete by user_id
if user_id is not None:
    end_test = delete_user(user_id)
    print(f"User {name} with ID {user_id} deleted successfully.")
else:
    print(f"New user not found in DB, user: {name}")
