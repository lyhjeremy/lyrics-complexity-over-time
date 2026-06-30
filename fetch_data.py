"""
fetch_data.py - download the Billboard Year-End Hot 100 lyrics, 1964-2015.

Source: walkerkq/musiclyrics (public). Columns: Rank, Song, Artist, Year, Lyrics,
Source. Lyrics are lowercased with punctuation stripped. Saved to ./data/.
"""
import os
import urllib.request

URL = "https://raw.githubusercontent.com/walkerkq/musiclyrics/master/billboard_lyrics_1964-2015.csv"
OUT = os.path.join(os.path.dirname(__file__), "data", "billboard_lyrics_1964-2015.csv")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    print(f"Downloading {URL}")
    urllib.request.urlretrieve(URL, OUT)
    print(f"Saved -> {OUT} ({os.path.getsize(OUT):,} bytes)")


if __name__ == "__main__":
    main()
