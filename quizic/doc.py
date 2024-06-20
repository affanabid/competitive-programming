import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException


client_id = '1a38052d065540548b253c0920ee0a20'
client_secret = '138f810abcd14faa81849e33741384ac'
redirect_uri = 'http://example.com'
scope = 'playlist-modify-public'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Create a new playlist
playlist_name = input("Enter the playlist name: ")
user_id = sp.me()['id']
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

print(f"Playlist '{playlist_name}' created with ID: {playlist['id']}")

# Get a list of playlists from the current user's account
playlists = sp.current_user_playlists()
playlists_dict = {}
for playlist in playlists['items']:
    playlists_dict[playlist['name']] = playlist['id']

for name, id in playlists_dict.items():
    print(f"Name: {name}, ID: {id}")

def playlist_exists(playlist_id):
    try:
        # Attempt to get the playlist information
        playlist = sp.playlist(playlist_id)
        return True
    except SpotifyException as e:
        if e.http_status == 404:
            return False
        else:
            raise

playlist_name = input("Enter the playlist name: ")
playlist_id = playlists_dict[playlist_name]

playlist_id = '6RLmaiL3gl93UI6dhS9qyc'
exists = playlist_exists(playlist_id)
if exists:
    print(f"Playlist with ID {playlist_id} exists.")
else:
    print(f"Playlist with ID {playlist_id} does not exist.")

def search_and_add_to_playlist(song_name, playlist_id):
    try:
        # Search for the song
        results = sp.search(q=song_name, type='track', limit=1)
        tracks = results['tracks']['items']
        
        if not tracks:
            print(f"No tracks found for {song_name}")
            return
        
        # Get the track ID of the first result
        track_id = tracks[0]['id']
        
        # Add the track to the specified playlist
        sp.playlist_add_items(playlist_id, [track_id])
        print(f"Added {song_name} to playlist with ID {playlist_id}")
    except SpotifyException as e:
        print(f"Error adding song to playlist: {e}")

# Example usage
song_name = input("Enter the song name: ")
playlist_id = '6RLmaiL3gl93UI6dhS9qyc'  # Replace with the ID of the playlist you want to add the song to
search_and_add_to_playlist(song_name, playlist_id)