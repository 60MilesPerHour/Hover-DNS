import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from twilio.rest import Client
from twocaptcha import TwoCaptcha
import requests

load_dotenv()

# Load environment variables
HOVER_USERNAME = os.getenv("HOVER_USERNAME")
HOVER_PASSWORD = os.getenv("HOVER_PASSWORD")
TWO_CAPTCHA_API_KEY = os.getenv("TWO_CAPTCHA_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
USER_PHONE = os.getenv("USER_PHONE")

# Set up browser options
options = webdriver.ChromeOptions()
service = ChromeService(executable_path='/home/miles/Webscraping/chromedriver')
options.add_argument('--headless')
browser = webdriver.Chrome(service=service, options=options)

# Get the public IP address
ip = requests.get('https://api.ipify.org').text
print("This is your new public IP: " + ip)

# Open the hover.com login page
browser.get('https://www.hover.com/signin')
print("Logging in to hover.com...")
time.sleep(5)

# Login process
username = browser.find_elements('xpath', '//*[@id="app"]/div/form/div/div[1]/div/label/div[2]/div[1]/input')
username[0].send_keys(HOVER_USERNAME)
password = browser.find_elements('xpath', '//*[@id="app"]/div/form/div/div[2]/div/label/div[2]/div[1]/input')
password[0].send_keys(HOVER_PASSWORD)
time.sleep(5)
browser.find_element('xpath', '//*[@id="app"]/div/form/div/div[3]/div[2]/button').click()

# Check for CAPTCHA and solve if present
time.sleep(5)
if browser.find_elements('xpath', '//*[@id="rc-imageselect"]'):
    solver = TwoCaptcha(TWO_CAPTCHA_API_KEY)
    with open('captcha.png', 'rb') as captcha_file:
        captcha_response = solver.solve(captcha_file)
        captcha_solution = captcha_response['code']

    captcha_input = browser.find_element_by_name('captcha')
    captcha_input.send_keys(captcha_solution)
    submit_button = browser.find_element_by_name('submit')
    submit_button.click()

    # Send a Twilio notification about CAPTCHA
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(body="CAPTCHA Detected. Please check.", from_=TWILIO_PHONE, to=USER_PHONE)
else:
    print("No CAPTCHA present. Continuing...")

print("Login successful! Updating DNS records...")

# Define a list of domains to be updated (redacted for privacy)
domain_urls = os.getenv("DOMAINS").split(',')

for domain in domain_urls:
    browser.get(domain)
    time.sleep(5)

    # Update DNS records
    browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/ul/li[2]/a').click()
    time.sleep(2)

    # Update * Record
    browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div[7]/div').click()
    browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').clear()
    browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').send_keys(ip)
    print("Your * DNS record has been updated to: " + ip)
    browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[2]/button[2]').click()

    # Update @ Record
    browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[3]/div[7]/div').click()
    browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').clear()
    browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').send_keys(ip)
    print("Your @ DNS record has been updated to: " + ip)
    browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[2]/button[2]').click()

    time.sleep(5)
    browser.get('https://www.hover.com/control_panel')
    time.sleep(5)

    if domain == domain_urls[-1]:
        print("All DNS records have been updated!")
        browser.quit()
    else:
        print("Next domain...")
        time.sleep(5)
