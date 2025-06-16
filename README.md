# CozmoSpotifyNowPlaying
now playing for the anki cozmo robot
i've only tested this setup on windows, but it should work on other operating systems.
# installation
## setup
for an ideal experience, connect to cozmo wifi through a wifi card or a cheap adapter, since this isnt very intensive, and use ethernet to connect to your main internet.

make sure to have python 3.7.9 installed, other versions might work but i havent tested.
(could be from the microsoft store, or from python directly)
## creating the spotify app
use [this](https://developer.spotify.com) link to log in with your spotify account and create an app by clicking on your account in the top right, and selecting dashboard
## installing libraries
once installed, run this command in the terminal to install the neccessary libraries for spotify and cozmo

``` pip install spotipy pycozmo ```

# usage and such
when running, you should be directed to a spotify site letting you log in through your web browser,