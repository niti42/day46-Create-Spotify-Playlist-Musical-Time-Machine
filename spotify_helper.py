from dotenv import load_dotenv
import os
from pprint import pprint
import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
APP_REDIRECT_URI = "http://example.com"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=APP_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="Nithish Kumar CV", ))


def search_spotify_for_track(name, year='', artist='', num_results=10):
    query = f"track: {name} year: {year} artist: {artist}"
    print(query)

    search_results_dict = sp.search(
        query, limit=num_results)

    request_url = search_results_dict.get('tracks').get('href')
    search_results = search_results_dict.get('tracks').get('items')

    result_filtered = []
    for result in search_results:
        record = {
            "request_url": request_url,
            "song_name": result.get('name'),
            "artist_name": [artist.get('name')
                            for artist in result.get('album').get('artists')],
            "release_date": result.get('album').get('release_date'),
            "external_urls": result.get('external_urls').get('spotify'),
            "id": result.get('id'),
            "uri": result.get('uri')
        }
        result_filtered.append(record)
    return result_filtered


def spotify_playlist(playlist_name, track_uris):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False,
                                       collaborative=False, description='')
    # Extract the playlist ID
    playlist_id = playlist['id']
    # Add tracks to the playlist
    sp.user_playlist_add_tracks(
        user=user_id, playlist_id=playlist_id, tracks=track_uris)

    print(
        f"Playlist id '{playlist_id}' created successfully with {len(track_uris)} songs.")
