from spotipie import playlist_songs, token
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Playlist ID can be found through the browser; format is: https://open.spotify.com/playlist/6vbczC62GBq65CYelMn8M2
# and it is the last section, so here would be 6vbczC62GBq65CYelMn8M2
PLAYLIST_ID = YOUR PLAYLIST ID
#Username found through Spotify account
USERNAME = YOUR USERNAME
song_list = playlist_songs(PLAYLIST_ID)
# Creates a spotify object that authorizes the user when called
spotifyObject = spotipy.Spotify(auth_manager=token)


# determines length of playlist for future use
PLAYLIST_LENGTH = len(song_list)

# initializes list that will correspond to each playlist song
song_values = []

# assigns a value of zero to each song, which will later be added to
for i in range(PLAYLIST_LENGTH):
    song_values.append(0)

# Asks for a name and description of the new playlist
name = input("What do you wish the playlist to be called? ")
description = name + " in order"

# creates the new playlist in the users Spotify account
spotifyObject.user_playlist_create(user=USERNAME, name=name, description=description, public=True)

# compares each song to each other song. If you prefer one song, it gets
# a point added to its value
for j in range(PLAYLIST_LENGTH):
    for i in range(PLAYLIST_LENGTH - 1):
        i += 1
        if i > j:
            preference = int(input(f"do you prefer {song_list[j]} or {song_list[i]}? type 0 for first and 1 for second "))
            if preference == 0:
                song_values[j] += 1
            else:
                song_values[i] += 1
        else:
            pass

# initializes ordered list
ordered_songs = []

# adds songs in order by their value; song that was preferred the most times has the highest score,
# and song that was preferred least has the lowest score
for i in range(PLAYLIST_LENGTH):
    # determines highest score from list
    highest_rank = max(song_values)
    # loop that checks for which song has highest score
    for j in (range(PLAYLIST_LENGTH - len(ordered_songs))):
        if song_values[j] == highest_rank:
            # adds songs to ordered list and removes it from song lists
            ordered_songs.append(song_list[j])
            song_values.pop(j)
            song_list.pop(j)
            # breaks loop when highest score found
            break
        else:
            pass

# must change format of song to fit Spotify API
ordered_songs_for_input = []
for i in ordered_songs:
    search = spotifyObject.search(q=i)
    song = search['tracks']['items'][0]['uri']
    ordered_songs_for_input.append(song)

# finds playlist that was just created
findingPlaylist = spotifyObject.user_playlists(user=USERNAME)
playlist = findingPlaylist['items'][0]['id'] 
# adds ordered songs to new playlist
spotifyObject.user_playlist_add_tracks(user=USERNAME, playlist_id=playlist, tracks=ordered_songs_for_input)