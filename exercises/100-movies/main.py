def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Get movie titles
title_tags = soup.select("h3.title")
titles = [title.getText() for title in title_tags]

# print(*titles, sep="\n")

# Write to file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in reversed(titles):
        file.write(title + '\n')