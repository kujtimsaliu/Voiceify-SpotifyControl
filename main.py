import os
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# SPOTIPY_CLIENT_ID = os.getenv("69c8f80efb5f44dda08519da20f0d1e6")
# SPOTIPY_CLIENT_SECRET = os.getenv("92e51f68f5234c85858f16e76894d702")
# SPOTIPY_REDIRECT_URI = os.getenv("http://localhost:8888/callback")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-modify-playback-state user-read-playback-state"))

r = sr.Recognizer()

def play_pause_music():
    current_track = sp.current_playback()
    if current_track is None:
        print("No track is playing.")
        return

    if current_track['is_playing']:
        sp.pause_playback()
        print("Music paused.")
    else:
        sp.start_playback()
        print("Music resumed.")

def next_track():
    sp.next_track()
    print("Next track.")

def previous_track():
    sp.previous_track()
    print("Previous track.")

def search_spotify(query):
    results = sp.search(q=query, type='track,album,artist,playlist')
    return results

def adjust_volume(volume_percent):
    sp.volume(volume_percent)

def voice_search():
    with sr.Microphone() as source:
        print("Listening for search query...")
        audio = r.listen(source)
        query = r.recognize_google(audio)
        print(f"Received search query: {query}")

        # Search Spotify based on the query
        results = search_spotify(query)

        # Process and display search results
        for track in results['tracks']['items']:
            print(f"Track: {track['name']}")
            print(f"Artist: {', '.join([artist['name'] for artist in track['artists']])}")
            print(f"Album: {track['album']['name']}")
            print(f"Spotify URI: {track['uri']}")
            print()

def voice_volume_control():
    with sr.Microphone() as source:
        print("Listening for volume command...")
        audio = r.listen(source)
        command = r.recognize_google(audio).lower()
        print(f"Received volume command: {command}")

        if "increase volume" in command:
            adjust_volume(50)  # Increase volume by 50%
        elif "decrease volume" in command:
            adjust_volume(30)  # Decrease volume by 30%
        else:
            print("Volume command not recognized.")

def main():
    with sr.Microphone() as source:
        print("Listening for commands...")
        while True:
            try:
                audio = r.listen(source)
                command = r.recognize_google(audio).lower()
                print(f"Received command: {command}")

                if "pause" in command:
                    play_pause_music()
                elif "play" in command:
                    play_pause_music()
                elif "next" in command:
                    next_track()
                elif "previous" in command:
                    previous_track()
                elif "search" in command:
                    voice_search()
                elif "volume" in command:
                    voice_volume_control()
                elif "quit" in command:
                    break
                else:
                    print("Command not recognized.")

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()


