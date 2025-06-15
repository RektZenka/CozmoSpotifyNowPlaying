import cozmo
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# --- Spotify Authentication ---
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="3f7af9c417d14d4dbe2c5bee5ac4e3e0",
    client_secret="78a1fdc4469040c4b24786592d648c4b",
    redirect_uri="https://9f64-140-177-114-116.ngrok-free.app/callback",
    scope="user-read-playback-state"
))

def get_current_track():
    current = sp.current_playback()
    if current and current.get('item'):
        track = current['item']['name']
        artist = current['item']['artists'][0]['name']
        return f"{track} - {artist}"
    return "Nothing Playing"
# --- Cozmo Display Function ---
def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello! Spotify now playing!").wait_for_completed()
    while True:
        now_playing = get_current_track()
        robot.display_oled_face_text(now_playing[:15], 1.0)  # Limit text length for display
        time.sleep(5)

cozmo.run_program(cozmo_program)
