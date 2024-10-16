import os
import requests
from names_generator import generate_name
from db_connector import get_all_users, delete_user
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

try:
    # Test for posting new user to users database
    name = generate_name()
    URL = os.getenv("REST_URL")
    payload = {"user_name": f"{name}"}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(URL, json=payload, headers=headers)

    # Check posted data was stored inside DB
    all_users = get_all_users()
    user_id = None
    for user in all_users:
        if user['user_name'] == name:
            print(f"{name} found, backend test finish successfully")
            user_id = user['user_id']
            break

    BaseURL = f"{os.getenv('WEB_URL')}{user_id}"
    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BaseURL)
    delay = 5

    # Test for name element works properly with selenium
    try:
        element = WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.ID, "user")))
        print(f"Element found: {element.text}, frontend test finish successfully")
    except NoSuchElementException:
        print("Element not found.")
    driver.quit()

    # If user is found, delete by user_id
    if user_id is not None:
        end_test = delete_user(user_id)
        print(f"User {name} with ID {user_id} deleted successfully, combined test finish successfully!")
    else:
        print(f"New user not found in DB, user: {name}")
except Exception:
    print("Combined test failed")