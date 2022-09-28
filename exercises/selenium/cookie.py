def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pprint import pprint as pp
import time

# Create a Chrome driver
chrome_driver_path = "W:\GIT\TOOLS\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

# ------------------- COOKIE CLICKER -------------------------

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Click this cookie!
cookie_button = driver.find_element(By.ID, 'cookie')



# Function that clicks the cookie for 5 seconds
def click_cookie():
    
    # 5 seconds from now
    countdown = time.time() + 5

    while time.time() < countdown:
        cookie_button.click()
    
# Purchase the most expensive item that can be afforded
def shop():
    
    # Scrape data
    cookies = driver.find_element(By.ID, 'money')
    cookies = int(cookies.text.replace(',',''))    
    items = driver.find_elements(By.CSS_SELECTOR, '#store b')
    
    for item in reversed(items):
        if item.text != '':
            cost = item.text.split(' - ')
            cost = int(cost[1].replace(',',''))
            # print(f"Purchasing price of {cost} with amount of cookies: {cookies}")
            if cookies >= cost:
                print(f'Purchasing: {item.text}')
                purchase_button = item.find_element(By.XPATH, './..')
                purchase_button.click()
                return

                    
            

# Run the program for an amount of time
program_timer = time.time() + 5 * 60

while time.time() < program_timer:

    # Click for 5 seconds
    click_cookie()

    # Check number of cookies and shop    
    shop()
    
    # Repeat


# Print score and quit
print(driver.find_element(By.ID, 'cps').text)
driver.quit()