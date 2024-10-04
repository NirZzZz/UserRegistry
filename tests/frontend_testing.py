import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv

load_dotenv()

BaseURL = f"{os.getenv("WEB_URL")}1"
print(BaseURL)
driver = webdriver.Chrome()
driver.get(BaseURL)
time.sleep(2)
try:  # Test for name element works properly with selenium
    element = driver.find_element(By.ID, "user")
    print(f"Element found: {element.text}")
except NoSuchElementException:
    print("Element not found.")
driver.quit()
