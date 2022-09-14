def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from bs4 import BeautifulSoup
import requests

# ------------------ SCRAPING A LOCAL FILE --------------------------

# Open using UTF8 encoding to get the emojis working
with open("website.html", encoding="utf8") as file:
    soup = BeautifulSoup(file, 'html.parser')


# print(soup.prettify())

# print(soup.title.string)

a_tags = soup.select("a")

for tag in a_tags:
    # print(tag.getText()) # get the link text
    print(tag.get("href")) # Get the href attribute value

# print(*a_tags, sep="\n")

heading = soup.find(name="h1", id="name") # Find a specific tag with ID
section_heading = soup.find(name="h3", class_="heading") # class_ is used to search for tag classes

print(section_heading)

# Searching for a deeply nested tag -- (Using CSS selectors)
company_url = soup.select_one(selector="p a")

print(company_url)

print("\n------------------------------------------------------\n")

# ------------------ LIVE WEB SCRAPING --------------------------

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, 'html.parser')

# Get scores
scores = soup.select(".score")

most_points = 0

# Find the highest score
for score in scores:
    points = int(score.getText().split()[0])
    if(points > most_points):
        most_points = points
        top_score = score
        
# Get the top score ID
article_id = top_score.get("id").split("_")[1]

# Get the article Title and URL
top_article = soup.find(id=article_id).select("a.titlelink")[0]

print(f"{top_article.getText()} - {most_points} points")
print(top_article.get("href"))
print("\n")