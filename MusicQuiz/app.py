from flask import Flask, render_template, request, redirect, url_for, session
import random
import secrets
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

redirect_uri = 'http://127.0.0.1:5000/callback'
# scope = 'user-read-playback-state'
scope = 'user-read-playback-state user-modify-playback-state'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authorize', methods=['POST'])
def authorize():
    session['client_id'] = request.form['client_id'].strip()
    session['client_secret'] = request.form['client_secret'].strip()
    auth_manager = SpotifyOAuth(client_id=session['client_id'],
                                client_secret=session['client_secret'],
                                redirect_uri=redirect_uri,
                                scope=scope)
    auth_url = auth_manager.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    auth_manager = SpotifyOAuth(client_id=session['client_id'],
                                client_secret=session['client_secret'],
                                redirect_uri=redirect_uri,
                                scope=scope)
    code = request.args.get('code')
    try:
        token_info = auth_manager.get_access_token(code)
        session['token_info'] = token_info
    except spotipy.SpotifyOauthError as e:
        return f"SpotifyOauthError: {e.error}, description: {e.error_description}"
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    if 'token_info' not in session:
        return redirect(url_for('index'))
    return render_template('quiz.html')

@app.route('/play_quiz', methods=['POST'])
def play_quiz():
    artist_name = request.form['artist_name'].strip()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=session['client_id'],
                                                   client_secret=session['client_secret'],
                                                   redirect_uri=redirect_uri,
                                                   scope=scope,
                                                   cache_handler=spotipy.cache_handler.MemoryCacheHandler(session['token_info'])))
    random_tracks = get_random_songs(sp, artist_name)
    session['random_tracks'] = random_tracks
    session['score'] = 0
    session['current_track_index'] = 0
    return redirect(url_for('play_round'))

@app.route('/play_round')
def play_round():
    if 'random_tracks' not in session or session['current_track_index'] >= 10:
        return redirect(url_for('score_sheet'))

    # Get the current question number
    question_number = session['current_track_index'] + 1

    # Get the current score
    score = session['score']

    # Get the current track information
    current_track = session['random_tracks'][session['current_track_index']]
    track_name, track_uri = current_track

    # Start playback of the current track
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=session['client_id'],
                                                   client_secret=session['client_secret'],
                                                   redirect_uri=redirect_uri,
                                                   scope=scope,
                                                   cache_handler=spotipy.cache_handler.MemoryCacheHandler(session['token_info'])))
    data = sp.devices()
    DEVICE_ID = data['devices'][0]['id']
    sp.start_playback(device_id=DEVICE_ID, uris=[track_uri])

    # Render the play_round template with the current track information
    chances = session.get('chances', 3)
    return render_template('play_round.html', track=current_track, chances=chances, question_number=question_number, score=score)

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    guess = request.form['guess'].strip().lower()
    current_track_index = session['current_track_index']
    current_track = session['random_tracks'][current_track_index]
    score = session['score']
    question_number = current_track_index + 1
    if guess == current_track[0].lower():
        session['score'] += 1
        session['current_track_index'] += 1
        session.pop('chances', None)  # Reset chances for next track
        return redirect(url_for('play_round'))
    else:
        chances = session.get('chances', 3) - 1
        session['chances'] = chances
        if chances == 0:
            session['current_track_index'] += 1
            session.pop('chances', None)  # Reset chances for next track
            return redirect(url_for('play_round'))
        return render_template('play_round.html', track=current_track, chances=chances, question_number=question_number, score=score)

@app.route('/score_sheet')
def score_sheet():
    score = session.get('score', 0)
    return render_template('score_sheet.html', score=score)

def get_random_songs(sp, artist_name, limit=10):
    results = sp.search(q=f'artist:{artist_name}', type='track', limit=50, market='US')
    tracks = results['tracks']['items']
    if not tracks:
        return []
    random_tracks = random.sample(tracks, min(limit, len(tracks)))
    track_results = [(track['name'], track['uri']) for track in random_tracks]
    return track_results


if __name__ == '__main__':
    app.run(debug=True)
