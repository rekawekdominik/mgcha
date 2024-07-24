from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time
import argparse
import secrets

print("Mobilus Python Control")

parser = argparse.ArgumentParser(description='Mobilus Python Control - dummy app for blinds control')
parser.add_argument('device', type=str, help='Device to be used eg: Gabinet 1')
parser.add_argument('direction', type=str, help='Direction UP or DOWN')
parser.add_argument('--gateway', type=str, default=secrets.URL, help='URL of login page of Cosmo GTW')
args = parser.parse_args()

service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(args.gateway)

time.sleep(3)

username_field = driver.find_element(By.ID, "loginInput")
password_field = driver.find_element(By.ID, "passwordInput")

username_field.send_keys(secrets.USERNAME)
password_field.send_keys(secrets.PASSWORD)

password_field.send_keys(Keys.RETURN)

time.sleep(3)

element_xpath = "//div[contains(text(), '"+args.device+"')]"
div_element = driver.find_element(By.XPATH, element_xpath)
parent_element = div_element.find_element(By.XPATH, "./..")
up_control_element = parent_element.find_element(By.CLASS_NAME,"uparrow-btn")
down_control_element = parent_element.find_element(By.CLASS_NAME,"downarrow-btn")

print("From:" + args.gateway + " use: " + args.device)
if (args.direction=="UP"):
    print("Direction: up")
    up_control_element.click()
else:
    print("Direction: down")
    down_control_element.click()

driver.quit()