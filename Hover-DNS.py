from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import requests

# Create a new ChromeOptions object
options = webdriver.ChromeOptions()

# Set up the ChromeDriver executable path
service = ChromeService(executable_path='/home/miles/Webscraping/chromedriver')

# Set up for headless execution
options.add_argument('--headless')

# Create a new Chrome webdriver instance with the above options and service
browser = webdriver.Chrome(service=service, options=options)

# Get the public IP address using the requests library
ip = requests.get('https://api.ipify.org').text
print("This is your new public IP: " + ip)

# Open the hover.com login page
browser.get('https://www.hover.com/signin')

# Find the username field and enter the username
print("Logging in to hover.com...")
time.sleep(5)
username = browser.find_elements('xpath', '//*[@id="app"]/div/form/div/div[1]/div/label/div[2]/div[1]/input')
username[0].send_keys('USERNAME')

# Find the password field and enter the password
password = browser.find_elements('xpath', '//*[@id="app"]/div/form/div/div[2]/div/label/div[2]/div[1]/input')
password[0].send_keys('PASSWORD')

# Wait for 5 seconds
time.sleep(5)

# Find the login button and click it
browser.find_element('xpath', '//*[@id="app"]/div/form/div/div[3]/div[2]/button').click()

# Wait for 5 seconds
time.sleep(5)

# Print message indicating successful login and updating of DNS records
print("Login successful! Updating DNS records...")

# Find the domain name and click it
browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div[2]/a').click()

# Wait for 5 seconds
time.sleep(5)

# Find the DNS records and update them
browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(2)

# Update the * DNS record
browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div[7]/div').click()
time.sleep(2)
browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').clear()
browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').send_keys(ip)
print("Your * DNS record has been updated to: " + ip)
browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[2]/button[2]').click()

# Update the @ DNS record
browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[3]/div[7]/div').click()
time.sleep(2)
browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').clear()
# Update the @ DNS record
browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[1]/div[2]/div[3]/label/div[2]/div[1]/input').send_keys(ip)
print("Your @ DNS record has been updated to: " + ip)
browser.find_element('xpath', '/html/body/div[4]/div/div/div/form/div/div[2]/button[2]').click()

# Wait for 5 seconds
time.sleep(5)

# Print message indicating successful update of DNS records
print("DNS records updated successfully! now exiting...")

# Close the browser
browser.quit()
