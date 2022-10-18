from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from fastapi import FastAPI
import spotipy
import os

load_dotenv()
app = FastAPI()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv(CLIENT_ID),
        client_secret=os.getenv(CLIENT_SECRET),
        redirect_uri="http://127.0.0.1/callback/",
        scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])

@app.get("/")
async def root():
    return {"message": "Hello World"}