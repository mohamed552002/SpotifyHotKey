import time
from pywinauto import Desktop
class Spotify:
    spotify_window =""
    def __init__(self) -> None:
        pass
    def GetSpotifyWindow(self):
        for window in Desktop(backend="uia").windows():
            time.sleep(0.1)
            if "Spotify Free" == window.window_text() or "Spotify" == window.window_text():
                global spotify_window
                self.spotify_window = window
                break
        else:
            raise RuntimeError("Spotify window not found")
    def Toggle(self):
        if(self.spotify_window == ""):
            self.GetSpotifyWindow()
        self.spotify_window.restore()
        self.spotify_window.type_keys('{SPACE}')
        self.spotify_window.minimize()
        time.sleep(0.1)  
    def Next(self):
        self.spotify_window.restore()
        time.sleep(0.3)
        self.spotify_window.type_keys("^{RIGHT}")
        self.spotify_window.minimize()
    def Previuos(self):
        self.spotify_window.restore()
        time.sleep(0.1)
        self.spotify_window.type_keys("^{LEFT}")
        time.sleep(0.6)
        self.spotify_window.type_keys("^{LEFT}")
        self.spotify_window.minimize()