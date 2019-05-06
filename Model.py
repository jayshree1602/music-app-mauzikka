from cx_Oracle import *
class model():
    def __init__(self):
        self.song_dict={}
        self.db_status= True
        self.conn=None
        self.cur=None
        try:

            self.conn=connect("mouzika/music@rattu-PC/orcl")
            print("connect sucessfully to DB")
            self.cur = self.cursor()

        except:
            DatabaseError
    def get_db_status(self):
        return self.db_status
    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("cursor closed sucessfully")

        if self.conn is not None:
            self.conn.close()
            print("Disconnect sucessfully from the DB")

    def add_song(self,song_name,song_path):
        self.song_dict[song_name]=song_path
        print("song added:",self.song_dict[song_name])


    def get_song_path(self,song_name):
        return self.song_dict[song_name]


    def remove_song(self,song_name):
        self.song_dict.pop(song_name)
        print(self.song_dict)

    def search_song_in_favourites(self,song_name):
        self.cur.execute("Select song name from myfavourites where song_name=:1",(song_name,))
        song_tuple=self.cur.fetchone()
        if song_tuple is None:
            return False
        else:
            True
        #check kr lena

    def add_song_to_favourites(self,song_name,song_path):
        is_song_present=self.search_song_in_favourites(song_name)
        if is_song_present:
            return "Song already present in your favourites "

        self.cur.execute("select max(song_id) from myfavourites ")
        last_song_id=self.cur.fetchone()[0]
        next_song_id=1
        if last_song_id is not None:
            next_song_id=last_song_id+1

        self.cur.execute("insert into my favourites values (:1,:2,:3)", (next_song_id,song_name,song_path))
        self.conn.commit()
        return "Song added to your favourites"

    def add_song_to_favourits(self,song_name):
        song_path= self.my_model.get_song_path(song_name)
        result_self.my_model.add_song_to_favourites(song_name,song_path)
        return result

    def load_songs_from_favourites(self,song_name):
        self.cur.execute("select one song_name,song_path from myfavourites ")
        songs_present = False
        for song_name, song_path in self.cur:
            self.song_dict[song_name]=song_path
            sons_present=True
        if songs_present==True:
            return "List populated from favourites"
        else:
            reurn "No songs present there"

    #jo sir ne likhwaya
    def

    def remove_song_from_favourites(self,song_name):

