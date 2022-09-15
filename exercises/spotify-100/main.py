def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp


# --------------------- SPOTIFY -------------------
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_URI = os.environ.get("SPOTIFY_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=SPOTIFY_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

# ------------------------- PROGRAM ----------------------------

target_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")

billboard_URL = f"https://www.billboard.com/charts/hot-100/{target_date}/"

print(billboard_URL)

response = requests.get(billboard_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape the page and get a list of top 100 songs
title_tags = soup.select("div.o-chart-results-list-row-container li.lrv-u-width-100p ul li h3#title-of-a-story")

song_list = []

for title in title_tags:
    number = (title_tags.index(title)) + 1
    song_title = title.getText().strip()
    artist = title.find_next_sibling("span").getText().strip()
    
    song_list.append((song_title, artist))
    
# ------------------------------------------------------------------

# Search spotify and add song URIs to a new list
uri_list = []
year = target_date.split("-")[0]

for song in song_list:
    try:
        result = sp.search(q=f"{song[0]} by {song[1]}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except:
        print(f"Song URI not found for {song[0]} by {song[1]}.")

# ------------------------------------------------------------------

# Create playlist
new_playlist = sp.user_playlist_create( user=sp.current_user()["id"],
                                        name=f"{target_date} TOP 100 TRACKS",
                                        public=False,
                                        description=f"The Billboard top 100 tracks the week of {target_date}")

sp.user_playlist_add_tracks(
    user=sp.current_user()["id"],
    playlist_id=new_playlist['id'],
    tracks=uri_list,
    position=None    
)