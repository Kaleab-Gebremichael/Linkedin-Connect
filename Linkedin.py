from selenium import webdriver
from getpass import getpass

browser = webdriver.Chrome()

FILE_NAME = "linkedin_contacts.txt"

browser.get("https://www.linkedin.com/login")

#username = input("Enter in your linkedin username: ")
#password = getpass("Enter your password: ")
file = open("credentials.txt", "r")
allLines = file.readlines()

username = allLines[0].strip()
password = allLines[1].strip()


usernameTextbox = browser.find_element_by_id("username")
usernameTextbox.send_keys(username)

passwordTextbox = browser.find_element_by_id("password")
passwordTextbox.send_keys(password)

signInButton = browser.find_element_by_tag_name("button")
signInButton.click()

# open file containing links
file = open(FILE_NAME, "r")
allLinks = file.readlines()
link = ""   #initialize it as string to use the string methods

for link in allLinks:
    trimmedLink = link.strip()
    sendInvite(trimmedLink)

def sendInvite(userLink):
    # browser.get("https://www.linkedin.com/in/kaleab-gebremichael")
    browser.get(userLink)
