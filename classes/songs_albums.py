Songs = []
Song_Lists = {} #I could feature as an attribute

import random
class Song(object):

    def __init__(self, title, artist, duration, genre, music_file=""):
        self.title = title
        self.artist = artist
        duration = float(duration)
        self.duration = duration
        self.genre = genre
        self.music_file = music_file
        Songs.append(self)

    def __str__(self):
        return "{title} featuring {artist}, Play Time: {duration}".format(title=self.title, artist=self.artist, duration=self.duration)

    def play_song(self):
        print(self.title,"is playing...")

ALBUMS = []
class Album(object):
    #these all are class functions so they can only be used with their class but general functions can used with anything
    def __init__(self, album, song_list, label, published):
        self.album = album
        self.song_list = song_list
        self.label = label
        self.published = published
        ALBUMS.append(self)

    
    def __str__(self):
        #album_duration = 0
        #for song in self.song_list:
        #    int(song.duration)
        #    album_duration + song.duration
        #add this: Total Duration: {album_duration} & this: album_duration=self.album_durarion
        return "{album} featuring artists".format(album=self.album)

    def play_random(self):
        print(random.choice(self.song_list), "is playing...")
    

#I'm ceratin this is going to fail cause of memory location but what doesn't kill you makes stronger
#General functions
def random_song():
    rand_album = random.choice(ALBUMS)
    rand_songs = rand_album.song_list
    #rand_list = random.choice(Song_Lists)
    #rand_song = random.choice(rand_list)
    print(random.choice(rand_songs), "is playing from a random album...")

def random_album():
    print(random.choice(ALBUMS), "is playing...")
def print_album():
    for album in ALBUMS:
        print(album)

#This is me also trying figure out how name variable through user input
#def get_list_title():
#    title = input("Enter the name you would like to name this list")
#    return title

def Create_Song_List(title, songs):
    #I'm trying how to figure out how to make a list with it's variable being the title and the value the list of songs so I can call it by its variable name for songs lists
    # but if try use the variable i will just change the value of that variable 
    #This solution is for me to turn this into a dictionary
    
    Song_Lists.update({title: songs})