class Music_Library(object):

    def __init__(self, song_list, album_list=[], playlist_list=[]):
        self.song_list = song_list
        self.album_list = album_list
        self.playlist_list = playlist_list
    
    def print(self):
        print("Songs:")
        for song in self.song_list:
            print(song)

        print("Albums:")
        for album in self.album_list:
            print(album)

        print("Playlists:")
        for playlist in self.playlist_list:
            print(playlist)

    def __str__(self):
        #return "Songs: {}\nAlbums: {}\nplaylists: {}".format(self.song_list, self.album_list, self.playlist_list) you can't use two return statements
        return "Use the print function asscotiated with this class instead like so: My_Music.print()"
    
    def add_album(self, album):
        album_list = [item for item in self.album_list] 
        album_list.append(album)
        self.album_list = album_list
    
    def remove_album(self, album):
        album_list = [item for item in self.album_list] 
        album_list.remove(album)#Should i use pop instead ause a album could have the same name but be by two diferent artists
        self.album_list = album_list
    
    def add_playlist(self, playlist):
        playlist_list = [item for item in self.playlist_list] 
        playlist_list.append(playlist)
        self.playlist_list = playlist_list
        
    
    def remove_playlist(self, playlist):
        playlist_list = [item for item in self.playlist_list] 
        playlist_list.remove(playlist)
        self.playlist_list = playlist_list