from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver
driver = webdriver.Chrome()


# Navigate to the Telegram website
driver.get("https://web.telegram.org/k/")

# Wait for the website to load
time.sleep(5)

# Click phone signin
search_button = driver.find_element(
    By.XPATH, "//button[@class='btn-primary btn-secondary btn-primary-transparent primary rp']")
search_button.click()

# Wait for the website to load
time.sleep(5)

# Enter the phone number
search_box = driver.find_element(
    By.XPATH, "//div[@class='input-field input-field-phone']//div[@class='input-field-input']")
phone_number = "7553223567"  # Replace with the phone number you want to search for
search_box.send_keys(phone_number)

search_button = driver.find_element(
    By.XPATH, "// button[@class='btn-primary btn-color-primary rp']//div[@class='c-ripple']")
search_button.click()
print("helloo")
# driver1 = webdriver.Chrome()
# driver1.get("https: // www.truecaller.com/search/in / {phone_number}")
# Click on google button

# search_button = driver1.find_element(
#     By.XPATH, "// a[@class ='flex-1 cursor-pointer block h-60px flex items-center font-opensans font-semibold uppercase text-xs text-white text-center leading-none bg-brand rounded overflow-hidden truncate']")
# search_button.click()
# print("helloo")

# google_button = driver1.find_element(
#     By.XPATH, "//a[@data-test='GoogleSignIn']")
# google_button.click()
# print("hello")
# google_window = driver1.window_handles[1]
# driver1.switch_to.window(google_window)


# # Click on my google account
# search_button = driver1.find_element(
#     By.XPATH, "// button[@class ='r78aae TrZEUc']")
# search_button.click()

# Wait for the results page to load
time.sleep(20)
# Enter Phone number as input

# Click search button

# driver1.get("https: // www.truecaller.com/search/in / {phone_number}")
# # Locate the name of the person on the results page and extract it
name_element = driver.find_element(
    By.XPATH, "//div[@class='phone-wrapper']")

if name_element:
    print("User Exists")
else:
    print("User does not exists")


# # Print the name of the person
# print(f"The name of the person with phone number {phone_number} is {name}.")

# Close the browser
driver.quit()
# driver1.quit()
