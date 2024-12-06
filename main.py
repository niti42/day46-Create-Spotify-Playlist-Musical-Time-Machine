from billboard_scraper import get_billboard100_date
from spotify_helper import search_spotify_for_track, spotify_playlist
import json
from pprint import pprint


def compile_tracks(date):
    bb100 = get_billboard100_date(date)
    for title in bb100:
        name = title.get('song')
        artist = title.get('artist')

        year = date.split("-")[0]

        try:
            result = search_spotify_for_track(
                name, year, artist, num_results=1)[0]
        except IndexError:
            continue
        title["uri"] = result.get('uri')
        # title["sp_song_name"] = result.get('name')
        # title["sp_artist_name"] = result.get('artist_name')
        # title["release_date"] = result.get('release_date')
    return bb100


date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD :")
playlist_name = f"{date} Billboard 100"
bb100_week = compile_tracks(date)
track_uris = [song.get("uri") for song in bb100_week if song.get("uri")]

spotify_playlist(playlist_name, track_uris)
