from classes.songs_albums import Song, ALBUMS, Album, print_album, random_album, random_song, Create_Song_List, Song_Lists, Songs
from classes.playlists import playlists, Playlist
from classes.music_library import Music_Library
print("THE PROGRAM IS STARTING")

Devil_Be_After_Me = Song(title= "Devli_Be_After_Me", artist=["Cle Gbaby", "Young Moose", "Ziggy Ziya"], duration=4.54, genre="Hip Hop")
print(Devil_Be_After_Me)
Devil_Be_After_Me.play_song()

ball = Song(title= "20 ball", artist= "bandhunta izzy", duration=4.54, genre="Hip Hop")
All_In = Song(title= "All In", artist= "Yella Beezy", duration=3.54, genre="Hip Hop")
Vibe = Song(title= "Vibe", artist= ["bandhunta izzy", "Dream Doll"], duration= 2.32, genre="Hip Hop")
OTW = Song(title= "OTW", artist= ["bandhunta izzy", "Zonnique"], duration=2.00, genre="Hip Hop")


Create_Song_List(title = "Invite", songs = [ball, All_In])
Create_Song_List(title = "Devil Be After Me", songs = [Vibe, OTW])


for list in Song_Lists:#works
    print(list)

print("*" * 75, "printing songs")#doesn't work I left in so I could see how it doesn't work
print(Songs)

print("*"*75, "for song in song")#works
for song in Songs:
    print(song)
    

print("*"*75, "song lists")
print(Song_Lists)


Invite_Only = Album("Invite Only", song_list=["20 Ball", "All In", "Vibes", "OTW", "Something Different", "Guwop", "Bacc 'N Forth", "Givenchy", "40 Bars"], 
label="Bandhunta Izzy", published="March 27, 2020")

artists=["Bandhunta Izzy", "Yella Beezy", "YFN Lucci", "Dream Doll", "Zonnique", "Derez Dashawn", "Hoodrich Pablo Juan", "Bandhunta Jugg", 
"Young Crazy", "Jay Fizzle", "YFN Kay", "Sambo"]

doodoo_brown = Album(album="Doo Doo", song_list=["doo", "Doo", "brown"], label="DooDoo brown Records", published = 2003)


artists="Mr.Doodoo Brown"
print("*" * 75)
print(Invite_Only)
Invite_Only.play_random()
random_album()
random_song()
#print_album() #this just throws a weird message but everything so far works and just gives you the location in memory
###############################################################################################################################################################################

Baltimore_Anthems = Playlist("Baltimore Anthems", ["Devil Be After Me", "Bad Habits", "Bankrolls Remix", "Baltimore", "BBB", "Cut Throat Money", "Bread Hunters",
                             "Unorthodox", "With My Team", "Yip", "Nacho Bangers", "In The Field", "Panda", "KIng Me", "Bird Flu", "Dumb Dumb", "Bad and Boujee Gmix", 
                             "YSN", "What I Got"])
print(Baltimore_Anthems)                             
Baltimore_Anthems.print_playlist()

#Baltimore_Anthems.sort_help() it says it doesn't work because i passed in a arguement but i didn't

print(Baltimore_Anthems)
Baltimore_Anthems.remove_song("Baltimore")
Baltimore_Anthems.add_song("How We Living")
Baltimore_Anthems.print_playlist()


#using a seperate list of lists should help me pair artists with the songs
###############################################################################################################################################################################
My_Music = Music_Library(song_list=Songs, album_list=[doodoo_brown])

My_Music.add_album(Invite_Only)
My_Music.add_playlist(Baltimore_Anthems)

My_Music.print()

My_Music.remove_album(Invite_Only)
My_Music.remove_playlist(Baltimore_Anthems)

My_Music.print()