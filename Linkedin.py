from selenium import webdriver
from getpass import getpass

browser = webdriver.Chrome()


browser.get("https://www.linkedin.com/login")

username = input("Enter in your linkedin username: ")
password = getpass("Enter your password: ")

usernameTextbox = browser.find_element_by_id("username")
usernameTextbox.send_keys(username)

passwordTextbox = browser.find_element_by_id("password")
passwordTextbox.send_keys(password)

signInButton = browser.find_element_by_tag_name("button")
signInButton.click()

# links will go here
browser.get("https://www.linkedin.com/in/kaleab-gebremichael")
