#songs = {}
playlists = {}
class Playlist(object):
    
    def __init__(self, title, song_list):
        self.title = title
        self.song_list = song_list
        #songs.update({title:})
        playlists.update({title: len(song_list)})

    def __str__(self):
        return "Playlist: {}, Song Count: {}\n".format(self.title, len(self.song_list))
        
    
    def print_playlist(self):
        for song in self.song_list:
            print("{}".format(song))# featuring: {} , song.artist wanted to add this but would work with variable unless I created a func for specific cases like this
        print("*" * 70, "\n")
        
    def add_song(self, song):
        self.song_list.append(song)
    
    def remove_song(self, song):
        self.song_list.remove(song)

    def sort_help():
        print("You can sort your playlist by the artist, title, year, genre and even by the duration of the song")
    
   # def sort(self, sort="title"):
    #
    #    def title(x):
    #        return x[title]
    #    def artist(x):
    #        return x[artist]
    #    def playtime(x):
    #        return x[playtime]
    #    def genre(x):
    #        return x[genre]
    #    def year(x):
    #        return x[year]
        
    #    elif sort == "title":
    #        song_list.sort(key=title)
    #    elif sort == "artist":
    #        song_list.sort(key=artist)
    #    elif sort == "playtime":
    #        song_list.sort(key=playtime)
    #    elif sort == "genre":
    #        song_list.sort(key=title)
    #    elif sort == "year":
    #        song_list.sort(key=year)
    #    else: 
    #         print("{} is an invalid answer")
