# Voiceify-SpotifyControl
Enhance Your Spotify Experience with Voice Commands

![Voiceify Logo](voiceify-logo.png)

Voiceify is a voice-controlled Spotify player that allows you to control your Spotify music using voice commands. With Voiceify, you can play, pause, skip tracks, adjust the volume, and even search for your favorite songs, artists, and albums, all without lifting a finger.

## Features

- **Voice Playback Control:** Start, pause, resume, and skip tracks using voice commands.
- **Volume Adjustment:** Control the music volume with voice commands.
- **Voice Search:** Search for songs, artists, albums, or playlists using natural language.
- **Music Information:** Get information about the currently playing track.
- **User-Friendly Interface:** An intuitive voice-driven interface for a seamless music experience.

## Technologies Used

- **Python:** The core programming language for app development.
- **Spotipy:** A Python library for Spotify's Web API.
- **SpeechRecognition:** Python library for voice recognition.
- **dotenv:** Used for managing environment variables.
- **Spotify Web API:** Enables access to Spotify's music catalog and user playback control.
- **OAuth 2.0:** Used for secure authentication with the Spotify API.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kujtimsaliu/voiceify.git
   cd voiceify

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Set up your Spotify API credentials in a .env file:
SPOTIPY_CLIENT_ID=your-client-id
SPOTIPY_CLIENT_SECRET=your-client-secret
SPOTIPY_REDIRECT_URI=your-redirect-uri


Usage
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Start using voice commands to control your Spotify playback and discover music.

Voice Commands
Play: Start or resume playback.
Pause: Pause the music.
Next: Skip to the next track.
Previous: Go back to the previous track.
Search: Initiate a voice-based search for songs, artists, albums, or playlists.
Volume: Adjust the music volume (e.g., "increase volume" or "decrease volume").
Quit: Exit the application.


Make sure to replace  `your-client-id`, `your-client-secret`, and `your-redirect-uri` with your actual Spotify API credentials.


Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the app's functionality or fix bugs.
