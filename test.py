import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "b1ea5a3ed14042f0a469349ffde84652"
client_secret = "0459a4f8100746ddb52ac4eab93725f6"

saba_uri= "spotify:artist:7Hjbimq43OgxaBRpFXic4x"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

saba = sp.artist(saba_uri)
print("The artist", saba["name"], "has released the following albums:")


results = sp.artist_albums(saba_uri, album_type='album')

saba_albums = results["items"]
while results['next']:
    results = sp.next(results)
    saba_albums.extend(results['items'])

for a in saba_albums:
    print(a['name'])
