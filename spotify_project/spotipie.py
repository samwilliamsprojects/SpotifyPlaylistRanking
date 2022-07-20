import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

PLAYLIST_LENGTH = 10 
SCOPE = "playlist-modify-public"
USERNAME = YOUR USERNAME
PLAYLIST_ID = YOUR PLAYLIST ID

# parameters to authorize a user using SpotifyOAuth
token = SpotifyOAuth(
    scope=SCOPE, 
    username=USERNAME,
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://localhost:8888/callback" # uses local host for testing
)

# Creates a spotify object that authorizes the user when called
spotifyObject = spotipy.Spotify(auth_manager=token)

def playlist_songs(playlist_id):
    """
    Collects all song titles and their artist from a users Spotify playlist
    :param playlist_id: the playlist ID, URL or URI
    """
    playlist_tracks = spotifyObject.playlist_tracks(playlist_id=playlist_id)
    song_list = []
    j = 0
    # loop to add each song to the song list
    for i in range(PLAYLIST_LENGTH):
        song_list.append(playlist_tracks['items'][j]['track']['name'])
        j += 1

    # loop to add each artist to the artist list
    artist_list = []
    k = 0
    for l in range(PLAYLIST_LENGTH):
        artist_list.append(playlist_tracks['items'][k]['track']['album']['artists'][0]['name'])
        k += 1

    # combines song and artist
    for i in range(PLAYLIST_LENGTH):
        song_list[i] = song_list[i] + " by " + artist_list[i]

    return song_list

