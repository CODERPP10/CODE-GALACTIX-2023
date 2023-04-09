from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def login():
    print("Connecting to Telegram Web, please wait")

    browser = webdriver.Firefox(executable_path='/usr/bin/geckodriver')


    browser.get("https://web.telegram.org/#/login")

    sleep(3)

    phone_input_code = browser.find_element_by_name("phone_country")
    phone_input_number = browser.find_element_by_name("phone_number")

    country_code = input("Country code: ")
    phone_number = input("Phone number: ")

    phone_input_code.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + country_code + Keys.ENTER)
    phone_input_number.send_keys(Keys.BACKSPACE + phone_number + Keys.ENTER)

    # Wait for the page to load
    sleep(5)

    confirm_input = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[4]/input")
    confirm_code = input("Confirmation code (sent via SMS): ")
    confirm_input.send_keys(confirm_code + Keys.ENTER)

    sleep(5)
    password_input = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[1]/input")
    password_send = input("Please Login Password:")
    password_input.send_keys(password_send + Keys.ENTER)
    return browser