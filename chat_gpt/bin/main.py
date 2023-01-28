import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

# Replace with your Spotify API client ID and client secret
client_id = "ecf41aae00a9431989c8b10d37b391a8"
client_secret = "04ed59fdf6814eacbf7e24b33d3e09bc"



# Authenticate with the Spotify API
token = spotipy.util.prompt_for_user_token(client_id,
                                               client_secret)
client_credentials_manager = SpotifyClientCredentials(auth=token)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Retrieve the user's liked songs
spotif
results = spotify.current_user_saved_tracks()
tracks = results['items']
while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])

# Store the tracks and their genres in a dictionary
track_genres = {}
for track in tracks:
    track_id = track['track']['id']
    track_info = spotify.track(track_id)
    track_genres[track_id] = track_info['genres']

# Sort the tracks by genre
sorted_tracks = sorted(track_genres.items(), key=lambda x: x[1])

# Print the sorted list of tracks and genres
pprint.pprint(sorted_tracks)
