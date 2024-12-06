# Billboard Hot 100 Playlist Generator

This project allows you to generate a Spotify playlist based on the Billboard Hot 100 chart for a specified date. It scrapes the Billboard website for the top 100 songs of the specified week and adds them to a new Spotify playlist.

## Prerequisites

- Python 3.x
- Spotipy library for interacting with the Spotify Web API
- BeautifulSoup library for web scraping
- Requests library for making HTTP requests

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

   ```bash
   pip install spotipy beautifulsoup4 requests
   ```

3. Set up your Spotify API credentials:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new application.
   - Note down your `client_id`, `client_secret`, and `redirect_uri`.

## Configuration

Set up your Spotify API credentials in your environment variables:

```bash
export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client_secret'
export SPOTIPY_REDIRECT_URI='your_redirect_uri'
```

## Usage

Run the script and follow the prompts to generate your Spotify playlist:

```python main.py

```

## Example:

You will be prompted to enter a date in the format YYYY-MM-DD. The script will scrape the Billboard Hot 100 chart for that date and create a Spotify playlist with the top 100 songs.

## Acknowledgements

**Billboard** for providing the Hot 100 chart data.
**Spotify** for their API and platform.
