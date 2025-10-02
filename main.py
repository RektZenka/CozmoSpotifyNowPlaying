#----------------
# fuckass code
#----------------
import pycozmo
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from PIL import Image, ImageDraw, ImageFont
client_id = input("enter your spotify client id from the app you created earlier: ")
client_secret = input("enter your spotify client secret from the app you created earlier: ")

spotify_redirect_uri = "http://127.0.0.1:8888"

print(f"Using Spotify Redirect URI: {spotify_redirect_uri}")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id,
    client_secret,
    redirect_uri=spotify_redirect_uri,
    scope="user-read-playback-state"
))

def get_current_track():
    try:
        current = sp.current_playback()
        if current and current.get('item'):
            track = current['item']['name']
            artist = current['item']['artists'][0]['name']
            return f"{track} - {artist}"
    except Exception as e:
        print(f"Error getting current track from Spotify: {e}")
    return "Nothing Playing"

def cozmo_program():
    with pycozmo.connect() as robot:
        print("Connected to Cozmo via PyCozmo!")

        # Set Cozmo's volume to maximum (1.0) for speech
        robot.set_volume(1.0)

        display_width = 128
        display_height = 32
        font_size = 12
        font_name = "arial.ttf"

        try:
            font = ImageFont.truetype(font_name, font_size)
        except IOError:
            print(f"Warning: Could not load '{font_name}'. Using default Pillow font.")
            font = ImageFont.load_default()

        last_displayed_text = ""

        # the fun part!!!
        while True:
            now_playing = get_current_track()
            print(f"Now Playing: {now_playing}")

            text_to_display = now_playing
            if len(text_to_display) > 18:
                text_to_display = text_to_display[:15] + "..."

            # Create a blank 1-bit (black and white) image
            img = Image.new('1', (display_width, display_height), color=0)
            draw = ImageDraw.Draw(img)

            bbox = draw.textbbox((0, 0), text_to_display, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            x = (display_width - text_width) / 2
            y = (display_height - text_height) / 2
            draw.text((x, y), text_to_display, font=font, fill=255)

            robot.display_image(img)

            last_displayed_text = now_playing

            time.sleep(5)

if __name__ == '__main__':
    cozmo_program()
