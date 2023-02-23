from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import requests

# Create a new ChromeOptions object
options = webdriver.ChromeOptions()

# Set up the ChromeDriver executable path
service = ChromeService(executable_path='/CHROMEDRIVER/PATH/GOES/HERE')

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
username = browser.find_elements('xpath', 'YOUR_XPATHS')
username[0].send_keys('USERNAME')

# Find the password field and enter the password
password = browser.find_elements('xpath', 'YOUR_XPATHS')
password[0].send_keys('PASSWORD')

# Wait for 5 seconds
time.sleep(5)

# Find the login button and click it
browser.find_element('xpath', 'YOUR_XPATHS').click()

# Wait for 5 seconds
time.sleep(5)

# Print message indicating successful login and updating of DNS records
print("Login successful! Updating DNS records...")

# Find the domain name and click it
browser.find_element('xpath', 'YOUR_XPATHS').click()

# Wait for 5 seconds
time.sleep(5)

# Find the DNS records and update them
browser.find_element('xpath', 'YOUR_XPATHS').click()
time.sleep(2)

# Update the * DNS record
browser.find_element('xpath', 'YOUR_XPATHS').click()
time.sleep(2)
browser.find_element('xpath', 'YOUR_XPATHS').clear()
browser.find_element('xpath', 'YOUR_XPATHS').send_keys(ip)
print("Your * DNS record has been updated to: " + ip)
# click the save button
browser.find_element('xpath', 'YOUR_XPATHS').click()

# Update the @ DNS record
browser.find_element('xpath', 'YOUR_XPATHS').click()
time.sleep(2)
browser.find_element('xpath', 'YOUR_XPATHS').clear()
# Update the @ DNS record
browser.find_element('xpath', 'YOUR_XPATHS').send_keys(ip)
print("Your @ DNS record has been updated to: " + ip)
# click the save button
browser.find_element('xpath', 'YOUR_XPATHS').click()

# Wait for 5 seconds
time.sleep(5)

# Print message indicating successful update of DNS records
print("DNS records updated successfully! now exiting...")

# Close the browser
browser.quit()
