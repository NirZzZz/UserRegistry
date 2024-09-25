import requests
from names_generator import generate_name
from db_connector import get_all_users

# Test for posting new user to users database
name = generate_name()
URL = "http://127.0.0.1:5000/users"
payload = {"user_name": f"{name}"}
headers = {'Content-Type': 'application/json'}
r = requests.post(URL, json=payload, headers=headers)
print(r.text)

# Check posted data was stored inside DB
all_users = get_all_users()
if any(user['user_name'] == name for user in all_users):
    print(f"{name} found, test finish successfully")
else:
    print(f"new user not found in DB, user: {name}")
