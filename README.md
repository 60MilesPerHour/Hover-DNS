# Hover-DNS

## Hover.com DNS Updater

This is a Python script that uses the Selenium web driver to update your DNS records on Hover.com. You will need to have a Hover.com account and a domain name that you want to update. You will also need to download the ChromeDriver executable and specify the path to the executable in the script.

### Instructions

1. Open the `Hover-DNS.py` file in a text editor.

2. Replace the `USERNAME`, `PASSWORD`, and `CHROMEDRIVER_PATH` placeholders with your Hover.com username, password, and the path to your ChromeDriver executable.

3. Replace the `YOUR_XPATHS` placeholders with the appropriate XPath values for your Hover.com account. You can find these by inspecting the elements on the Hover.com website and copying the XPath value for each element.

4. Save the `Hover-DNS.py` file and run it using the following command: `` python3 Hover-DNS.py ``

5. The script will update the DNS records for your domain name on Hover.com using your public IP address. The script will print messages to the console indicating whether the login was successful and whether the DNS records were updated successfully.

### Note

This script is meant to serve as a starting point for updating your DNS records on Hover.com using Selenium. You will need to update the XPath values in the script with the appropriate values for your account. Also, keep in mind that Hover.com may change their website layout in the future, which may require updates to the script.
