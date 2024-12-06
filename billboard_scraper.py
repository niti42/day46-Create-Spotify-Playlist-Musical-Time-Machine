import requests
from bs4 import BeautifulSoup
import re
import json


USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}


def is_valid_name(s):
    # Check if the string is not a number and does not contain only special characters
    if s.isdigit() or re.fullmatch(r'[\W_]+', s):
        return False
    # Check if it contains at least one alphabetic character
    return bool(re.search(r'[A-Za-z]', s))


def get_billboard100_date(date):
    billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"
    resp = requests.get(billboard_url, headers=USER_AGENT)
    print(resp.status_code)
    billboard_hot100_page = resp.text

    soup = BeautifulSoup(billboard_hot100_page, "html.parser")

    # get all song names
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]

    # get all artist names
    artist_names_top_tag = soup.select("li ul li span")
    artist_names_pos = [tag.getText().strip() for tag in artist_names_top_tag]

    artist_names = [item for item in artist_names_pos if is_valid_name(item)]

    # Combine song names and artist names into a list of dictionaries
    songs_data = [{"song": song_names[i], "artist": artist_names[i]}
                  for i in range(min(len(song_names), len(artist_names)))]

    print(f"compiled list of: {len(songs_data)} songs")

    return songs_data


if __name__ == "__main__":
    from pprint import pprint
    # Write the data to a JSON file
    date = "1993-09-25"
    bb100_songs = get_billboard100_date(date)

    with open(f"billboard-hot100-{date}.json", "w") as json_file:
        json.dump(bb100_songs, json_file, indent=4)
