from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Set up the Chrome driver
driver = webdriver.Chrome()


# Navigate to the Telegram website
driver.get("https://www.oyorooms.com/login?country=&retUrl=/")

# Wait for the website to load
time.sleep(5)


search_box = driver.find_element(
    By.XPATH, "//input[@class='textTelInput__input']")
phone_number = "9767947654"  # Replace with the phone number you want to search for
search_box.send_keys(phone_number)

# Click phone signin
search_button = driver.find_element(
    By.XPATH, "//button[@class='loginCard__button']")
search_button.click()

# driver.get("https://www.oyorooms.com/login?country=&modal=signin&retUrl=%2F")
# name_element = driver.find_element(
#     By.XPATH, "//p[@class='otpCard__otpDesc']")

driver1 = webdriver.Chrome()
driver1.get('https://www.oyorooms.com/login?country=&modal=signup&retUrl=%2F')
name_element = driver.find_element(
    By.XPATH, "//div[@class='oyo-row oyo-row--no-spacing signUpCard']")

if name_element:
    print("User not Exists")
else:
    print("User exists")

driver.quit()
driver1.quit()
