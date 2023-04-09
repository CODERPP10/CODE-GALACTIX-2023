from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Truecaller website
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fb%3Fnode%3D2454169031%26pf_rd_r%3DSC9RPA4TE2129XHY5VYM%26pf_rd_p%3D3ea052be-9c86-42bd-97cb-7610e61dcb39%26pd_rd_r%3Dba85d501-d2f7-4968-864c-91b684f9d0e8%26pd_rd_w%3DHRg7e%26pd_rd_wg%3DAuSg0%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# Wait for the website to load
time.sleep(5)

# Locate the search box and enter the phone number
print("hello")
search_box = driver.find_element(By.XPATH, "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field a-form-error']")
phone_number = "9767947654"  # Replace with the phone number you want to search for
print("world")
search_box.send_keys(phone_number)

# Click the search button
search_button = driver.find_element(
    By.XPATH, "//div[@class='searchbar-button']//span[@class='a-button a-button-span12 a-button-primary']")
search_button.click()

# Wait for the results page to load
time.sleep(5)

# Locate the name of the person on the results page and extract it
name_element = driver.find_element(
    By.XPATH, "//a[@class='ProfileHeader-nameLink']")
name = name_element.text

# Print the name of the person
print(f"The name of the person with phone number {phone_number} is {name}.")

# Close the browser
driver.quit()
