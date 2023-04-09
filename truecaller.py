from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver
driver = webdriver.Chrome()


# Navigate to the Truecaller website
driver.get("https://www.truecaller.com/")

# Wait for the website to load
time.sleep(5)

# Locate the search box and enter the phone number

# Click the search button

# Accept Cookies
search_button = driver.find_element(
    By.XPATH, "//button[@class='btn border-2 border-brand !py-4 !px-6']")
search_button.click()

search_box = driver.find_element(
    By.XPATH, "//input[@class='rtl:text-right h-full flex-1 appearance-none min-w-0 bg-transparent border-none focus:ring-0 focus-visible:outline-none']")
phone_number = "9819048189"  # Replace with the phone number you want to search for
search_box.send_keys(phone_number)

search_button = driver.find_element(
    By.XPATH, "// button[@class ='bg-brand flex items-center justify-center flex-none text-white h-60px w-60px sm:h-70px sm:w-70px rounded-full p-0 m-2 hover:bg-dark-blue-400 transition disabled:bg-brand']")
search_button.click()

# Click on signin
# search_button = driver.find_element(
#     By.XPATH, "//button[@class='flex items-center whitespace-nowrap']")
# search_button.click()


driver1 = webdriver.Chrome()
driver1.get("https: // www.truecaller.com/search/in / {phone_number}")
# Click on google button

# search_button = driver1.find_element(
#     By.XPATH, "// a[@class ='flex-1 cursor-pointer block h-60px flex items-center font-opensans font-semibold uppercase text-xs text-white text-center leading-none bg-brand rounded overflow-hidden truncate']")
# search_button.click()
# print("helloo")

google_button = driver1.find_element(
    By.XPATH, "//a[@data-test='GoogleSignIn']")
google_button.click()
print("hello")
google_window = driver1.window_handles[1]
driver1.switch_to.window(google_window)


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
# name_element = driver1.find_element(
#     By.XPATH, "//a[@class='ProfileHeader-nameLink']")
# name = name_element.text

# # Print the name of the person
# print(f"The name of the person with phone number {phone_number} is {name}.")

# Close the browser
# driver.quit()
# driver1.quit()
