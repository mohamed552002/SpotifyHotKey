import keyboard
from Spotify import Spotify
spotify_functions = Spotify()
keyboard.add_hotkey('ctrl+*', spotify_functions.Toggle)
keyboard.add_hotkey('alt+ctrl+n', spotify_functions.Next)
keyboard.add_hotkey('alt+ctrl+p', spotify_functions.Previuos)

print("Press Ctrl+* to toggle Spotify playback")
keyboard.wait('esc')
