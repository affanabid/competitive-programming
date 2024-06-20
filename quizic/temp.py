from flask import Flask, redirect, request, session, url_for, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import time
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate and set a strong secret key
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setup', methods=['POST'])
def setup():
    session['client_id'] = request.form['client_id']
    session['client_secret'] = request.form['client_secret']
    session['redirect_uri'] = request.form['redirect_uri']

    sp_oauth = SpotifyOAuth(
        client_id=session['client_id'],
        client_secret=session['client_secret'],
        redirect_uri=session['redirect_uri'],
        scope='user-read-playback-state user-modify-playback-state'
    )

    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(
        client_id=session['client_id'],
        client_secret=session['client_secret'],
        redirect_uri=session['redirect_uri'],
        scope='user-read-playback-state user-modify-playback-state'
    )

    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect(url_for('quiz'))

def get_token():
    token_info = session.get("token_info", None)
    if not token_info:
        return redirect(url_for('login'))
    now = int(time.time())
    is_token_expired = token_info['expires_at'] - now < 60
    if is_token_expired:
        sp_oauth = SpotifyOAuth(
            client_id=session['client_id'],
            client_secret=session['client_secret'],
            redirect_uri=session['redirect_uri'],
            scope='user-read-playback-state user-modify-playback-state'
        )
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

@app.route('/quiz')
def quiz():
    token_info = get_token()
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    artist_name = request.args.get('artist')
    if not artist_name:
        return "Please provide an artist name.", 400
    
    tracks = get_random_songs(sp, artist_name)
    
    return render_template('quiz.html', tracks=tracks, artist_name=artist_name)

def get_random_songs(sp, artist_name, limit=10):
    results = sp.search(q=f'artist:{artist_name}', type='track', limit=50, market='US')
    tracks = results['tracks']['items']
    
    if not tracks:
        return []
    
    random_tracks = random.sample(tracks, min(limit, len(tracks)))
    track_results = []
    for track in random_tracks:
        data = {'name': track['name'], 'uri': track['uri']}
        track_results.append(data)
    return track_results

@app.route('/play/<track_uri>')
def play_song(track_uri):
    token_info = get_token()
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    devices = sp.devices()
    if not devices['devices']:
        return "No available devices found.", 400
    
    device_id = devices['devices'][0]['id']
    try:
        sp.start_playback(device_id=device_id, uris=[track_uri])
    except Exception as e:
        return f"Error playing song: {e}", 500
    
    return "Playing song."

if __name__ == '__main__':
    app.run(debug=True)
