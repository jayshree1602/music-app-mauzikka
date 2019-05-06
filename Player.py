import Model
from pygame import mixer
from tkinter import filedialog
import os
from mutagen.mp3 import MP3

class Player:
    def __init__(self):
        mixer.init()
        self.my_model=Model.model()


    def get_db_status(self):
        return self.my_model.get_db_status()

    def close_player(self):
        mixer.music.stop()
        self.my_model.close_db_connection()

    def set_volume(self,volume_level):
        mixer.music.set_volume(volume_level)

    def add_song(self):
        song_path=filedialog.askopenfilename(title="select your song...",filetypes=[("mp3 files",".mp3")])
        if song_path=="":
            return
        song_name=os.path.basename(song_path)
        print("song path is:",song_path)
        print("song name is:", song_name)
        self.my_model.add_song(song_name,song_path)
        return song_name

    def get_song_length(self,song_name):
        self.song_path=self.my_model.get_some_path(song_name)
        self.audio_tag=MP3(self.song_path)
        song_length=self.audio_tag.info.length
        return song_length


if __name__=="__main__":
    p=Player()
    print("DB Conn:",p.get_db_status())
    p.add_song()