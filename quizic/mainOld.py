import random, spotipy
from spotipy.oauth2 import SpotifyOAuth
from random import sample

client_id = input("Enter your Spotify client ID: ").strip()
client_secret = input("Enter your Spotify client secret: ").strip()
# client_id = '1a38052d065540548b253c0920ee0a20'
# client_secret = '138f810abcd14faa81849e33741384ac'
redirect_uri = 'http://example.com'
scope = 'user-read-playback-state'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

def get_random_songs(artist_name, limit=10):
    results = sp.search(q=f'artist:{artist_name}', type='track', limit=50, market='US')
    tracks = results['tracks']['items']
    
    if not tracks:
        print(f"No tracks found for {artist_name}.")
        return
    
    random_tracks = random.sample(tracks, min(limit, len(tracks)))
    track_results = []
    for track in random_tracks:
        data = (track['name'], track['uri'])
        track_results.append(data)
    # print(f"Random songs by {artist_name}:")
    # for idx, track in enumerate(random_tracks, start=1):
    #     print(f"{idx}. {track['name']}")
    return track_results

def play_song(song_name, artist_name=None, device_id=None):
    query = f"track:{song_name}"
    if artist_name:
        query += f" artist:{artist_name}"
    
    results = sp.search(q=query, type='track', limit=1)
    tracks = results['tracks']['items']
    
    if not tracks:
        print(f"No tracks found for {song_name}.")
        return
    
    track_uri = tracks[0]['uri']
    sp.start_playback(device_id=device_id, uris=[track_uri])

# # Example usage
# device_id = '7b109b714fa1c644be10d03bbe360a0be00e2289'
# song_name = input("Enter the song name: ")
# artist_name = input("Enter the artist name (optional): ")
# play_song(song_name, artist_name, device_id)

# print(sp.devices())

def play_quiz(tracks):
    score = 0
    continuee = True
    for i in range(10):
        chances = 3

        track_name = tracks[i][0]
        track_uri = tracks[i][1]
        # Play the song
        sp.start_playback(device_id = '7b109b714fa1c644be10d03bbe360a0be00e2289',uris=[track_uri])
        
        # Get user's guess
        
        
        # Check if the guess is correct
        while True:
            guess = input(f"{i+1}. Guess the song ({chances} chances left): ")
            if guess.lower() == track_name.lower():
                print("Correct!")
                score += 1
                break
            else:
                chances -= 1
                print("Wrong! Try again.")
                if chances == 0:
                    print(f"Out of chances. The correct answer was: {track_name} by {artist_name}")
                    continuee = False
                    break
        
        print(f'Sccore: {score}/10\n')

    print(f"Game over. Your score is: {score}")


artist_name = input("Enter the artist's name: ")
random_tracks = get_random_songs(artist_name)
play_quiz(random_tracks)


