"""
Create a music player web app:
* Users can create audio using URLs available online.
* Users can create multiple Playlists based on the genre of the song.
* Users can add multiple audio files into each playlist created.
* Users can search audio by name.
* Users can search the playlist by name.
* Users can give ratings to playlist and audio. Rating displayed is the average rating calculated after each submission.

"""
class Music_Player: 
    #Constructor with initialized variables
    def __init__(self,user):
        self.user= user
        self.genre={}
        self.playlist_ratings = {}

    # Methods added for each functionality of the music player
    def create_playlist(self,playlist_name): 
        #Created a dictionary that contains the playlists for each user
        print(f"Creating playlist... {playlist_name} for {self.user}")
        self.playlist = []
        while True:
            song= str(input("Enter the name of the song (q to quit): ").lower())
            if song=='q':
                break
            else:
                self.playlist.append(song)
        self.genre[playlist_name]=self.playlist

    def search_music(self,playlist_name, song_name):
        print(f"Searching... {playlist_name} for {song_name}")
        if song_name in self.genre[playlist_name]:
            print("Result: Song found")
        else:
            print("Result: Song not found")

    def search_playlist(self,playlist_name):
        print(f"Searching... {playlist_name}")
        if playlist_name in self.genre.keys():
            print("Result: Playlist found")
        else:
            print("Result: Playlist not found")

    def view_playlist(self, playlist_name):
        print(f"The songs in {playlist_name} playlist are:")
        for song in self.genre[playlist_name]:
            print(song)

    def song_rating(self, playlist_name):
        self.song_ratings={} 
        #Created an empty dictionary that could hold the rating for every song.
        print(f"Rate the songs in {playlist_name} playlist")
        for song in self.genre[playlist_name]:
            print(f'Song Name: {song}')
            self.song_ratings[song]=int(input("Enter the rating of the song: "))

    def display_song_rating(self, playlist_name):
        average_rating = 0
        print(f"Playlist song ratings for {playlist_name}:")
        for song in self.genre[playlist_name]:
            print(f'{song:10} : {self.song_ratings[song]}')

        for song in self.genre[playlist_name]:
            average_rating+=self.song_ratings[song]

        print(f'Average Rating: {average_rating/len(self.genre[playlist_name]):.2f}')

    def playlist_rating(self, playlist_name):
        self.playlist_ratings[playlist_name]=int(input(f"Enter the rating of {playlist_name} playlist: "))

    def display_playlist_rating(self, playlist_name):
        print(f'Rating of the playlist {playlist_name} : {self.playlist_ratings.get(playlist_name)}')

#Objects defined with respective parameters
user1=Music_Player("User1")
user2=Music_Player("User2")

#Methods called for each functionality
user1.create_playlist('playlist1')
user1.create_playlist('playlist2')
# user1.create_playlist('playlist2')
# user1.view_playlist('playlist1')
# user1.search_music('playlist1', 'song1')
# user1.search_music('playlist1', 'songNull')
# user1.search_playlist('playlist1')
# user1.view_playlist('playlist1')
user1.song_rating('playlist1')
user1.display_song_rating('playlist1')
# user1.playlist_rating('playlist1')
# user1.playlist_rating('playlist2')
# user1.display_playlist_rating('playlist1')
# user1.display_playlist_rating('playlist2')

