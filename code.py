import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import datetime
import gspread

"""
Hello! Welcome to your very own Spotify Wrapped! 
This are the API's you will need to build your own Wrapped:
Spotify API     https://developer.spotify.com/documentation/web-api/
GSpread API     https://developers.google.com/sheets/api/quickstart/python

DESCRIPTION OF PROGRAM:
As the name suggest we are making a Spotify Wrapped, but unlike Spotify that allows access to us on a yearly bases you
can now access your top tracks when you want, the tracks gathered will be sent to google spread sheets where they are dived into
three categories: 
short_term = most recent top songs
medium_term = 6th month mark top songs
long_term = getting close to that year mark top songs

"""

## Authorization ##
SPOTIPY_CLIENT_ID='YOUR CLIENT-ID'
SPOTIPY_CLIENT_SECRET='YOUR CLIENT-SECRET'
#you can get the 2 above once you have created an account with Spotify for developers and created a new project
SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090'
SCOPE = "user-top-read"

# spotipy objects to access info #
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))


# print(sp.status_code)

## get top tracks ##
## try to format the dic output so its easier to read ##
top_tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range="short_term")
# print(top_tracks.json())
# print(top_tracks)



## getting songs ids from dic ##
def get_track_ids(time_frame):
    track_ids = []
    for song in time_frame['items']:
        track_ids.append(song['id'])
    return track_ids


## print out track ids ##
track_ids = get_track_ids(top_tracks)
print(track_ids)
print()


## fix error AttributeError: 'list' object has no attribute 'split' ##
def get_track_features(id):
    # pass track id
    meta = sp.track(id)
    name = meta['name']
    album = meta['album']['name']
    # 0 passed in case there are more artist featured
    artist = meta['album']['artists'][0]['name']
    # spotify url to open song directly in spotify
    spotify_url = meta['external_urls']['spotify']
    album_cover = meta['album']['images'][0]['url']
    track_info = [name, album, artist, spotify_url, album_cover]
    return track_info


## commenting this line allows for the code to work why? ##
## uncomment and you get error AttributeError: 'list' object has no attribute 'split' ##
print(get_track_features(track_ids[0]))


## insert data into sheets ##
def insert_to_gsheet(track_ids):
    # loop over track ids
    tracks = []
    for i in range(len(track_ids)):
        time.sleep(.5)
        track = get_track_features(track_ids[i])
        tracks.append(track)
    # create dataset
    df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'spotify_url', 'album_cover'])
    # insert into google sheet
    #path to your json file
    gc = gspread.service_account(r'C:\Users\...\spotify-wrapped-357717-e363bc73301f.json')
    sh = gc.open('Spotify Wrapped')
    worksheet = sh.worksheet(f'{time_period}')
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('Done')



time_ranges = ['short_term', 'medium_term', 'long_term']
for time_period in time_ranges:
    top_tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range=time_period)
    track_ids = get_track_ids(top_tracks)
    insert_to_gsheet(track_ids)
