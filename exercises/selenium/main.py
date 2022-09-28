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

# Create a Chrome driver
chrome_driver_path = "W:\GIT\TOOLS\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)


# -------------- AMAZON PRICE CHECK ------------------------

# driver.get("https://amzn.asia/d/5WugASH")

# # Get Price
# # cost_string = driver.find_element(By.CSS_SELECTOR, "span .a-price .a-offscreen")
# cost_string = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')

# print(f"The cost is: ${cost_string.text}")
# print("done")



# -------------- PYTHON PAGE EVENTS ------------------------
# Scrape the Event dates and information from the Python home page, and store in a dictionary

# driver.get("https://www.python.org/")

# # Get List of events using XPATH
# events_element = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# events_list = events_element.find_elements(By.TAG_NAME, 'li')

# # Save data to dictionary
# events_dict = {}

# for event in events_list:
#     index = events_list.index(event)
#     time = event.find_element(By.TAG_NAME, 'time').text
#     name = event.find_element(By.TAG_NAME, 'a').text
    
#     events_dict[index] = {'time':time, 'name':name}
    
# pp(events_dict)


# -------------- WIKI PAGE INTERACTION ------------------------
# Scrape the Event dates and information from the Python home page, and store in a dictionary

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(article_count.text)
# article_count.click()

# # Searching for link using the link text
# random_article = driver.find_element(By.LINK_TEXT, 'Random article')
# random_article.click()

## Typing in input fields
# search_bar = driver.find_element(By.NAME, 'search')
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)


# ----------------- FORM SIGN UP EXERCISE ---------------------
# Automatically fill out login information on a website

driver.get("http://secure-retreat-92358.herokuapp.com/")

# Get input fields
fname = driver.find_element(By.NAME, 'fName')
lname = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

# Typing in input fields
fname.send_keys("John")
lname.send_keys("Doe")
email.send_keys("johnDoe@learningpython.test")
email.send_keys(Keys.ENTER)



# driver.close() --> Closes a tab
# driver.quit() --> Quits the entire program
driver.quit()


