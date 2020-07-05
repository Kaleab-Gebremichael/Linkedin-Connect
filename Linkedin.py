from selenium import webdriver
from getpass import getpass

browser = webdriver.Chrome()

# file containing all linkedin links
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

def sendInvite(userLink):
    browser.get(userLink)
    connectButtonXpathLink = "/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button"
    connectKey = browser.find_element_by_xpath(connectButtonXpathLink)
    connectKey.click();

    doneButtonXpathLink = "/html/body/div[4]/div/div/div[3]/button[2]"
    doneKey = browser.find_element_by_xpath(doneButtonXpathLink)
    doneKey.click();


for link in allLinks:
    trimmedLink = link.strip()
    sendInvite(trimmedLink)


