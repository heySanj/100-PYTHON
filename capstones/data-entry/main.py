GOOGLE_FORM = "https://forms.gle/oxFXzNWxt7BRCMQ77"
ZILLOW = ('https://www.zillow.com/homes/for_rent/1-_beds/?'
          'searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22'
          'usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22'
          'west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734'
          '%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C'
          '%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value'
          '%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B'
          '%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%'
          '3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C'
          '%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3'
          'Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B'
          '%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C'
          '%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D')
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language":"en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive"
}

def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

# Import Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Beautiful Soup
import requests
from bs4 import BeautifulSoup


# ----------------- SCRAPE LISTINGS -----------------

# Get HTML
response = requests.get(ZILLOW, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape data
link_list = soup.find_all('a', {'data-test':'property-card-link','tabindex':'0'})
link_list = [("https://www.zillow.com" + (a['href']).replace('https://www.zillow.com','')) for a in link_list]

prices_list = soup.find_all('span', {'data-test':'property-card-price'})
prices_list = [(price.text.replace('+',' ').replace('/',' ').split(' '))[0] for price in prices_list]

address_list = soup.find_all('address', {'data-test':'property-card-addr'})
address_list = [address.text for address in address_list]


# -------------- DATA ENTRY ------------------

# Create a Chrome driver
chrome_driver_path = "W:\GIT\TOOLS\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

# Access the Google Form
driver.get(GOOGLE_FORM)

time.sleep(1)

# Loop through data and enter into the form
for n in range(len(address_list)):

    # Get input fields
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    # Typing in input fields
    address_input.send_keys(address_list[n])
    price_input.send_keys(prices_list[n])
    link_input.send_keys(link_list[n])
    submit.click()

    time.sleep(1)

    # Submit another
    another_submission = driver.find_element(By.LINK_TEXT, 'Submit another response')
    another_submission.click()


# # driver.close() --> Closes a tab
# # driver.quit() --> Quits the entire program
driver.quit()