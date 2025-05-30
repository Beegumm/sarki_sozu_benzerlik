import os
import time
import lyricsgenius
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# ✅ KULLANICININ TOKENI
GENIUS_API_TOKEN = "dovmGkabfY_lo1YOd-Uh1qy-wQYg7-vzmkp4utm0IJh7ZyVW0zukZQwXshpqJifA"

genius = lyricsgenius.Genius(GENIUS_API_TOKEN, skip_non_songs=True, remove_section_headers=True, timeout=10)
genius.verbose = False

SAVE_DIR = "data/raw"
os.makedirs(SAVE_DIR, exist_ok=True)

songs = [
    ("Bohemian Rhapsody", "Queen"),
    ("Imagine", "John Lennon"),
    ("Hotel California", "Eagles"),
    ("Smells Like Teen Spirit", "Nirvana"),
    ("Billie Jean", "Michael Jackson"),
    ("Like a Rolling Stone", "Bob Dylan"),
    ("Shape of You", "Ed Sheeran"),
    ("Hey Jude", "The Beatles"),
    ("Let It Be", "The Beatles"),
    ("Hallelujah", "Leonard Cohen"),
    ("What a Wonderful World", "Louis Armstrong"),
    ("Rolling in the Deep", "Adele"),
    ("Lose Yourself", "Eminem"),
    ("Stairway to Heaven", "Led Zeppelin"),
    ("Sweet Child O' Mine", "Guns N' Roses"),
    ("Someone Like You", "Adele"),
    ("Yesterday", "The Beatles"),
    ("All of Me", "John Legend"),
    ("Counting Stars", "OneRepublic"),
    ("Blank Space", "Taylor Swift"),
    ("Shallow", "Lady Gaga"),
    ("Take Me to Church", "Hozier"),
    ("Uptown Funk", "Mark Ronson"),
    ("Radioactive", "Imagine Dragons"),
    ("Bad Guy", "Billie Eilish"),
    ("Old Town Road", "Lil Nas X"),
    ("Thinking Out Loud", "Ed Sheeran"),
    ("Born to Die", "Lana Del Rey"),
    ("Fix You", "Coldplay"),
    ("Chandelier", "Sia")
]

def scrape_lyrics_from_url(url):
    try:
        page = requests.get(url)
        html = BeautifulSoup(page.text, "html.parser")
        lyrics = ""
        for tag in html.select("div[class^='Lyrics__Container']"):
            lyrics += tag.get_text(separator=" ").strip() + "\n"
        return lyrics.strip()
    except Exception as e:
        print(f"HATA: {e}")
        return ""

if __name__ == "__main__":
    for title, artist in tqdm(songs, desc="Şarkılar çekiliyor"):
        try:
            song = genius.search_song(title, artist)
            if song:
                lyrics = scrape_lyrics_from_url(song.url)
                filename = title.replace(" ", "_").lower() + ".txt"
                with open(os.path.join(SAVE_DIR, filename), "w", encoding="utf-8") as f:
                    f.write(lyrics)
                time.sleep(1.5)
            else:
                print(f"Bulunamadı: {title} - {artist}")
        except Exception as e:
            print(f"HATA ({title}): {e}")